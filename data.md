# GramEval Data 

All data available is stored in [CoNLL-U](https://universaldependencies.org/format.html) format:

'''
# newdoc
# newpar
# sent_id = 1
1	Кто	кто	PRON	_	Case=Nom	3	nsubj	_	_
2	нить	нить	NOUN	_	Animacy=Inan|Case=Nom|Gender=Fem|Number=Sing	1	appos	_	_
3	настраивал	настраивать	VERB	_	Aspect=Imp|Gender=Masc|Mood=Ind|Number=Sing|Tense=Past|VerbForm=Fin|Voice=Act	0	root	_	_
4	связку	связка	NOUN	_	Animacy=Inan|Case=Acc|Gender=Fem|Number=Sing	3	obj	_	_
5	VisualSVN	Visualsvn	PROPN	_	Foreign=Yes	4	flat:foreign	_	_
6	Server	Server	PROPN	_	Foreign=Yes	5	flat:foreign	_	_
7	+	плюс	PUNCT	_	_	6	punct	_	_
8	Trac	Trac	ADP	_	_	11	case	_	_
9	0.11	0.11	NUM	_	_	11	nummod	_	_
10	на	на	ADP	_	_	11	case	_	_
11	Windows?	Windows?	SYM	_	_	12	obl	_	_
12	Можете	мочь	VERB	_	Aspect=Imp|Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin|Voice=Act	4	acl:relcl	_	_
13	подсказать,	подсказать	ADV	_	Degree=Pos	12	advmod	_	_
14	а	а	CCONJ	_	_	19	cc	_	_
15	то	то	PRON	_	Animacy=Inan|Case=Nom|Gender=Neut|Number=Sing	19	mark	_	_
16	заводится	заводиться	VERB	_	Aspect=Perf|Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin|Voice=Mid	15	fixed	_	_
17	никак	никак	ADV	_	Degree=Pos	19	advmod	_	_
18	не	не	PART	_	_	19	advmod	_	_
19	хочет	хотеть	VERB	_	Aspect=Imp|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin|Voice=Act	12	conj	_	_
20	(((	(((	PUNCT	_	_	19	punct	_	_

'''

## Training Data

TBA

The organizers provide additional data with fully automatic annotation:

 - [Google Drive Link](https://drive.google.com/open?id=11713jFT1-xhPmrNinDQCj4vVn0jRn3XU) 

### MorphoRuEval 

Russian Corpus Data with manual verification, including SynTagRus, OpenCorpora, GICR, RNC.

Annotation:
 - unified automatic morphology (AOT, Mystem, ABBYY Compreno...)
 - UDPipe

### Twitter

Corpus of Russian tweets with sentiment annotation from [http://study.mokoron.com/](http://study.mokoron.com/)

Annotation:
 - UDPipe pipeline (tokenization, morphology, syntax)
 
### Wikipedia

Actual dump of [Russian Wikipedia](https://dumps.wikimedia.org/ruwiki/20200101/), first (will be supplemented)

Annotation:
 - UDPipe pipeline (tokenization, morphology, syntax)
