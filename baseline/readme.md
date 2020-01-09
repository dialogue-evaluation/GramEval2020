# Baseline

## Tokenization 

NLTK word tokenization https://www.nltk.org/api/nltk.tokenize.html

## Morphology

RNNMorph https://github.com/IlyaGusev/rnnmorph/
Morphological analyzer (POS tagger) for Russian and English languages based on neural networks and dictionary-lookup systems (pymorphy2, nltk).

Best in 2017 MorphoRuEval competition

## Russian UDpipe trained on SynTagRus

Download model from https://rusvectores.org/static/models/udpipe_syntagrus.model

## Example usage

```
from baseline import parse_text

parse_text('мама мыла раму')

>>
1	мама	мама	NOUN	_	Animacy=Anim|Case=Nom|Gender=Fem|Number=Sing	2	nsubj	_	_
2	мыла	мыть	VERB	_	Aspect=Imp|Gender=Fem|Mood=Ind|Number=Sing|Tense=Past|VerbForm=Fin|Voice=Act	0	root	_	_
3	раму	рама	NOUN	_	Animacy=Inan|Case=Dat|Gender=Masc|Number=Sing	2	iobj	_	_

```


Dependencies:
  - nltk
  - rnnmorph
  - ufal.udpipe
