
# coding: utf-8


import os, re
import sys
import argparse
import pyconll
from numpy import mean
from collections import Counter


def check_pair(gold_tag, test_tag):
    if re.sub('ё', 'е', gold_tag).lower()==re.sub('ё', 'е', test_tag).lower():
        return 1
    return 0

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
    syntax =  mean(uas)
    alignment_score = mean(alignment_score)
    return morphology, lemmatization, syntax, pos, {k:Counter(errors[k]).most_common(10) for k in errors},alignment_score


def main():
    parser = argparse.ArgumentParser(description='GramEval Test')
    parser.add_argument('test_file', type=str, help='Input dir for test file')
    parser.add_argument('gold_file', type=str, help='Input dir for gold file')
    args = parser.parse_args()
    if len(sys.argv) !=2: 
        print('evaluate.py <test_file> <gold_file>')
        #sys.exit(-1)

    print('loading files...')

    testfile = args.test_file
    goldfile = args.gold_file

    test_data = pyconll.load_from_file(testfile)
    gold_data = pyconll.load_from_file(goldfile)

    morph_score, lem_score, synt_score, pos_score, errors, alignment_score = compare(test_data, gold_data)

    quality = mean([morph_score, lem_score, synt_score])

    print('\nOverall quality:', quality)

    print('\nDetails:\n', '\nPOS quality:', pos_score,'\nMorphological features:', morph_score, '\nLemmatization:',lem_score, '\nUAS:', synt_score)

    print('\n Alignment score (should be 1.0, otherwise the tokenization is corrupted)', alignment_score, '\n')
    print(errors)

if __name__ == "__main__":
    main()


