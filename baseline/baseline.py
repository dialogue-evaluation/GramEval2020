#!/usr/bin/env python
# coding: utf-8


import ufal.udpipe
from rnnmorph.predictor import RNNMorphPredictor
from udpipe_model import Model

predictor = RNNMorphPredictor(language="ru")

# Download model from https://rusvectores.org/static/models/udpipe_syntagrus.model
model_file = 'udpipe_syntagrus.model'
model = Model(model_file)


def to_conllu(wordforms):
    lines = []
    for i in range(len(wordforms)):
        line = [str(i+1), wordforms[i].word, wordforms[i].normal_form, wordforms[i].pos,wordforms[i].tag]
        lines.append('\t'.join(line+['_']*5)  )
    return '\n'.join(lines)

def pipeline(tokens):
    forms = predictor.predict(tokens)
    sentences = model.read(to_conllu(forms), 'conllu')
    for s in sentences:
        model.tag(s)
        model.parse(s)
    return model.write(sentences, "conllu")

def parse_vertical_text(vertical_text):
    sents = vertical_text.split('\n\n')
    tokens = [[w.split('\t')[1] for w in s.split('\n') if '\t' in w] for s in sents]
    return [pipeline(tokenlist) for tokenlist in tokens]

# print(parse_vertical_text(your_vertical_conllu_text_here)[0])




