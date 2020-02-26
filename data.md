# GramEval Data 

All data available is stored in [CoNLL-U](https://universaldependencies.org/format.html) format:

```
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

```
Enhanced dependencies and empty/secondary nodes should not be part of the output. 

## Development Data (open test sets) 
* news [UD_MorphoRuEval2017](https://raw.githubusercontent.com/dialogue-evaluation/GramEval2020/master/dataOpenTest/GramEval2020-RuEval2017-Lenta-news-dev.conllu) 1K
* social networks [UD_MorphoRuEval2017](https://raw.githubusercontent.com/dialogue-evaluation/GramEval2020/master/dataOpenTest/GramEval2020-RuEval2017-social-dev.conllu) 1K
* wiki [UD_GSD](https://raw.githubusercontent.com/dialogue-evaluation/GramEval2020/master/dataOpenTest/GramEval2020-GSD-wiki-dev.conllu) 1K 
* fiction [UD_SynTagRus](https://raw.githubusercontent.com/dialogue-evaluation/GramEval2020/master/dataOpenTest/GramEval2020-SynTagRus-dev.conllu) 1K 
* poetry [UD_Taiga](https://raw.githubusercontent.com/dialogue-evaluation/GramEval2020/master/dataOpenTest/GramEval2020-Taiga-poetry-dev.conllu) 1K
* 17th century [UD_MidRussian-RNC](https://raw.githubusercontent.com/dialogue-evaluation/GramEval2020/master/dataOpenTest/GramEval2020-17cent-dev.conllu) 1K

## Training Data

### SynTagRus-UD

[UD_SynTagRus](https://raw.githubusercontent.com/dialogue-evaluation/GramEval2020/master/dataTrain/GramEval2020-SynTagRus-train.conllu)

[UD_SynTagRus-v02](https://raw.githubusercontent.com/dialogue-evaluation/GramEval2020/master/dataTrain/GramEval2020-SynTagRus-train-v2.conllu) - a harmonized version with semi-manual corrections 

Russian data from the SynTagRus corpus (1.1M tokens, fiction, news, wiki, nonficion).
Source: [UD Russian SynTagRus repository](https://github.com/UniversalDependencies/UD_Russian-SynTagRus)

Annotation:
 - automatic (ETAP3), human correction in native SynTagRus, then re-tokenized and converted automatically to UD 2.x 
 - enhanced dependencies removed, minor fixes of lemmas, UPOS, features, and relations 
 
### UD Russian GSD 

* wiki [UD_GSD](https://raw.githubusercontent.com/dialogue-evaluation/GramEval2020/master/dataTrain/GramEval2020-GSD-train.conllu) 

Russian Universal Dependencies Treebank annotated and converted by Google (96K tokens, wiki). 
Source: [UD_Russian GSD repository](https://github.com/UniversalDependencies/UD_Russian-GSD/tree/dev) 

Annotation:
 - automatic (GSD), human correction 
 
### UD Russian Taiga 

* social [UD_Taiga](https://raw.githubusercontent.com/dialogue-evaluation/GramEval2020/master/dataTrain/GramEval2020-Taiga-social-train.conllu) 26K
* poetry [UD_Taiga](https://raw.githubusercontent.com/dialogue-evaluation/GramEval2020/master/dataTrain/GramEval2020-Taiga-social-poetry.conllu) 13K
* news [UD_Taiga](https://raw.githubusercontent.com/dialogue-evaluation/GramEval2020/master/dataTrain/GramEval2020-Taiga-social-news.conllu) 0.3K

Samples extracted from Taiga Corpus and MorphoRuEval-2017 text collections (38K tokens, blog, social, poetry, news). 
[UD_Russian Taiga repository](https://github.com/UniversalDependencies/UD_Russian-Taiga/tree/dev) 

Annotation:
 - manual 

### MorphoRuEval 2017

* news [UD_RuEval2017](https://raw.githubusercontent.com/dialogue-evaluation/GramEval2020/master/dataTrain/MorphoRuEval2017-Lenta-train.conllu) (Lenta.ru, 5K)
* fiction [UD_RuEval2017](https://raw.githubusercontent.com/dialogue-evaluation/GramEval2020/master/dataTrain/MorphoRuEval2017-JZ-gold.conllu) (magazines.gorky.media, 7K)
* social [UD_RuEval2017](https://raw.githubusercontent.com/dialogue-evaluation/GramEval2020/master/dataTrain/MorphoRuEval2017-VK-gold.conllu) (VK, 5K)

Russian Corpus Data with manual verification, including SynTagRus, OpenCorpora, GICR, RNC.

Annotation:
 - unified automatic morphology (AOT, Mystem, ABBYY Compreno...)
 - UDPipe
 
### RNC 17th century 

* historical [UD_OldRussian-RNC](https://raw.githubusercontent.com/dialogue-evaluation/GramEval2020/master/dataTrain/GramEval2020-17cent-train.conllu) (dependencies manually corrected, 39K)
* historical [UD_OldRussian-RNC](https://yadi.sk/d/3osfa7ijEnE2Eg) (dependencies auto, 3,2M)

A subcorpus of the Middle Russian corpus, texts of the 17th century (4M tokens, business&law, letters, church slavic, hybrid) 

Annotation: 
  - upos and features: hybrid automatic with partial manual post-correction 
  - lemmas: TBA 
  - dependencies: automatic (UDpipe) 

## Additional Data

The organizers provide additional data with fully automatic annotation:

 - [Google Drive Link](https://drive.google.com/open?id=11713jFT1-xhPmrNinDQCj4vVn0jRn3XU) 

### MorphoRuEval 2017

[link](https://drive.google.com/file/d/1V3YGEHoE-2wY-5Qc-DIKwwa9q0yyOa5J/view?usp=sharing)

Russian Corpus Data with manual verification, including SynTagRus, OpenCorpora, GICR, RNC.

Annotation:
 - unified automatic morphology (AOT, Mystem, ABBYY Compreno...)
 - UDPipe
 
### Twitter

Updated [link](https://drive.google.com/file/d/1T8JPZISgkiR4wj53OycazTc3g0b0WCSO/view?usp=sharing)

Corpus of Russian tweets with sentiment annotation from [http://study.mokoron.com/](http://study.mokoron.com/)

Annotation:
 - UDPipe pipeline (tokenization, morphology, syntax)
 
### Wikipedia

[link](https://drive.google.com/file/d/1QZm__DREAndXL3PtQp1moLKPIzPecQlN/view?usp=sharing)

Actual dump of [Russian Wikipedia](https://dumps.wikimedia.org/ruwiki/20200101/), first 100000 articles (will be supplemented)

Annotation:
 - UDPipe pipeline (tokenization, morphology, syntax)
 
 ### Youtube comments
 
[link](https://drive.google.com/file/d/1aAGxWNNd0vXE3toJ4PYj7rV7qme3O7Ad/view?usp=sharing)
 
Comments from Russian Youtube Trends, april 2019
 
Annotation:
 - UDPipe pipeline (tokenization, morphology, syntax)

### Lenta Ru news

[link](https://drive.google.com/file/d/1pCBOICuxoPO-2Zqcai6jIhn7omaR7GTe/view?usp=sharing)
 
Lenta Ru news, up to 2018
 
Annotation:
 - symbol unification
 - UDPipe pipeline (tokenization, morphology, syntax)
 
### Stihi ru (Taiga)

[link](https://drive.google.com/file/d/1wsirY9vSIeF68vRUCxM3qxTwcKfFgxJY/view?usp=sharing)
 
Stihi ru poetry, part from from Taiga Corpus
 
Annotation:
 - symbol unification
 - UDPipe pipeline (tokenization, morphology, syntax)
 
### Proza ru (Taiga)

[link](https://drive.google.com/file/d/1ZvPuBO8ju6eU8WtYw2l15EH5L2CRwL3k/view?usp=sharing)
 
Proza ru fiction, part from from Taiga Corpus
 
Annotation:
 - symbol unification
 - UDPipe pipeline (tokenization, morphology, syntax)
 
### Fiction Magazines (Taiga)

[link](https://drive.google.com/file/d/1ehf5pc3MPu8b0RNN1JK5vmybGlWanVJ-/view?usp=sharing)
 
Materials from https://magazines.gorky.media/, Tiga Corpus
 
Annotation:
 - symbol unification
 - UDPipe pipeline (tokenization, morphology, syntax)
 
