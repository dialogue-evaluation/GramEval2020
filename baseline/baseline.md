# Baseline

## Tokenization 

## Morphology

## Russian UDpipe traied on syntagrus


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
