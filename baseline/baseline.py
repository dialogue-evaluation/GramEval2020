#!/usr/bin/env python
# coding: utf-8


from nltk import sent_tokenize, word_tokenize
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

def pipeline(sentence):
    tokens = word_tokenize(sentence)
    forms = predictor.predict(tokens)
    sentences = model.read(to_conllu(forms), 'conllu')
    for s in sentences:
        model.tag(s)
        model.parse(s)
    return model.write(sentences, "conllu")

def parse_text(text):
    sents = sent_tokenize(text)
    return [pipeline(s) for s in sents]

# print(parse_text('мама мыла раму')[0])




