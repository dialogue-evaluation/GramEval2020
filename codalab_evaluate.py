#!/usr/bin/env python
# coding: utf-8

import sys
import os, re
import os.path
import codecs
from conll import Conll
from numpy import mean
from collections import Counter
from io import open

sys.path.append(os.path.dirname(__file__))

def check_pair(gold_tag, test_tag):
    try:
        if re.sub('ё', 'е', gold_tag).lower()==re.sub('ё', 'е', test_tag).lower():
            return 1
        return 0
    except:
        return 0

def load_from_file(filename):
    """
    Load a CoNLL-U file given its location.

    Args:
        filename: The location of the file.

    Returns:
        A Conll object equivalent to the provided file.

    Raises:
        IOError: If there is an error opening the given filename.
        ParseError: If there is an error parsing the input into a Conll object.
    """
    with open(filename, encoding='utf-8') as f:
        c = Conll(f)

    return c


def compare(test, gold):
    lemma_counter, feat_counter, pos_counter = [], [], []
    las, uas = [], []

    alignment_score = []
    #Unlabeled attachment score (UAS) = percentage of correct head
    #Labeled attachment score (LAS) = percentage of correct head and dependency label

    errors = {'Syntax':[], 'POS':[], 'Morphology':[], 'Lemmas':[]}
    token_counter = sum([len(s) for s in gold])

    if len(test)!=len(gold):
        print('The amount of sentences you are passing does not correspond with number of sentences in gold set')
    #simple true-false classification
    for i in range(len(gold)):
        for j in range(len(gold[i])):
            try:

                alignment_score.append(check_pair(gold[i][j].form, test[i][j].form))

                check = check_pair(gold[i][j].lemma, test[i][j].lemma)
                lemma_counter.append(check)
                if not check:
                    errors['Lemmas'].append(test[i][j].lemma)

                check = check_pair(gold[i][j].head,test[i][j].head)
                uas.append(check)
                if check:
                    las.append(check_pair(gold[i][j].deprel,test[i][j].deprel))
                else:
                    las.append(0)
                    errors['Syntax'].append(test[i][j].deprel)
                check = check_pair(gold[i][j].upos, test[i][j].upos)
                pos_counter.append(check)
                if not check:
                    errors['POS'].append(test[i][j].upos)
                check = (sum([gold[i][j].feats[k]==test[i][j].feats[k] for k in gold[i][j].feats if k in test[i][j].feats])+0.00001)/(len(gold[i][j].feats.keys())+0.00001)
                feat_counter.append(check)
                if check!=1:
                    errors['Morphology'].append(test[i][j].form)
            except IndexError:
                lemma_counter.append(0)
                uas.append(0)
                las.append(0)
                pos_counter.append(0)
                feat_counter.append(0)
            #print(gold[i][j].upos)


    lemmatization = mean(lemma_counter)#(lemma_counter+0.00001)/(token_counter+0.00001)
    pos = mean(pos_counter)
    morphology = mean(feat_counter)
    syntax =  mean(las)
    alignment_score = mean(alignment_score)
    return morphology, lemmatization, syntax, pos, {k:Counter(errors[k]).most_common(10) for k in errors},alignment_score

def main():
    # as per the metadata file, input and output directories are the arguments
    [_, input_dir, output_dir] = sys.argv

    # unzipped submission data is always in the 'res' subdirectory

    test_dir = os.path.join(input_dir, 'res')
    gold_dir = os.path.join(input_dir, 'ref')

    if not os.path.isdir(test_dir):
        print("{0} doesn't exist".format(test_dir))

    if os.path.isdir(test_dir) and os.path.isdir(gold_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        output_filename = os.path.join(output_dir, 'scores.txt')
        output_file = codecs.open(output_filename, 'w', encoding='utf-8')
        html_filename = os.path.join(output_dir, 'scores.html')
        html_file = codecs.open(html_filename, 'w', encoding='utf-8')
        quality = []
        gold_list = os.listdir(gold_dir)
        for gold in gold_list:
            gold_file = os.path.join(gold_dir, gold)
            corresponding_test_file = os.path.join(test_dir, gold)
            if os.path.exists(corresponding_test_file):
                gold_data = load_from_file(gold_file)
                test_data = load_from_file(corresponding_test_file)
                morph_score, lem_score, synt_score, pos_score, errors, alignment_score = compare(test_data, gold_data)
                qual_score = mean([morph_score, lem_score, synt_score])
                quality.append(qual_score)

                html_string = '''<!DOCTYPE html>
                <html>
                <head>
                <style>
                table, th, td {
                  border: 1px solid black;
                  border-collapse: collapse;
                }
                th, td {
                  padding: 5px;
                  text-align: left;
                }
                </style>
                </head>
                <body>

                <h2>Results - %s</h2>

                <table border=1 style="width: auto; margin: 10px auto 0 auto;">
                  <tr>
                    <th>Metrics</th>
                    <th>Value</th>
                  </tr>
                  <tr>
                    <td>Overall quality</td>
                    <td>%s</td>
                  </tr>
                  <tr>
                    <td>POS quality</td>
                    <td>%s</td>
                  </tr>
                  <tr>
                    <td>Morphological features</td>
                    <td>%s</td>
                  </tr>
                  <tr>
                    <td>Lemmatization</td>
                    <td>%s</td>
                  </tr>
                  <tr>
                    <td>UAS</td>
                    <td>%s</td>
                  </tr>
                  <tr>
                    <td>Alignment score</td>
                    <td>%s</td>
                  </tr>
                </table>

                <h2>Errors</h2>
                <p>%s</p>

                </body>
                </html>''' % (gold, qual_score, pos_score, morph_score, lem_score, synt_score, alignment_score, errors)

                
                html_file.write(html_string)

        output_file.write("overall_quality:%s\n" % (mean(quality)))
        output_file.close()
        html_file.close()

if __name__ == "__main__":
    main()
