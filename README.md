# GramEval-2020

## A shared task on full morphology and dependency parsing of Russian texts 

### Дорожка по автоматическому морфологическому и синтаксическому анализу русских текстов

* [Codalab Link](https://competitions.codalab.org/competitions/22902?secret_key=38f3cda8-d1c4-427b-ba06-23ba44ff2264)
* Channel in Telegram: [@grameval2020](http://t.me/grameval2020) 
* [Paper](http://www.dialog-21.ru/media/5109/lyashevskayaonplusetal-181.pdf) and [slides](grameval_dialogue_slides.pdf) by organizers 

Collocated with [Dialog 2020](http://www.dialog-21.ru/evaluation/2019/disambiguation/grameval/)

The objective of the GramEval 2020 Shared Task is to process Russian texts starting from provided tokens to parts of speech (pos), grammatical features, lemmas, and labeled dependency trees. To encourage the multi-domain processing, five genres of Modern Russian are selected as test data: news, social media and electronic communication, wiki-texts, fiction, poetry; Middle Russian texts are used as the sixth test set. The data annotation follows the Universal Dependencies scheme. Unlike in many similar tasks, the collection of existing resources, the annotation of which is not perfectly harmonized, is provided for training, so the variability in annotations is a further source of difficulties. The main metric is the average accuracy of pos, features, and lemma tagging, and LAS.

GramEval 2020 — дорожка по оценке методов и технических решений для полного морфологического и синтаксического анализа текстов на русском языке. В 2020 году доминантой была выбрана жанровая репрезентативность текстового материала. Для оценки подходов к автоматическому анализу текста был подготовлен тестовый набор данных, охватывающий пять жанров современного языка: новости, сообщения из социальных
сетей и электронную коммуникацую, энциклопедические статьи, художественную литературу, поэзию, а также исторические тексты 17 века.

## GramEval Results 🏆
1. qbic - 0.91609 [link](https://github.com/DanAnastasyev/GramEval2020) [Anastasyev 2020](Exploring pretrained models for joint morpho-syntactic parsing of Russian)
2. ADVance - 0.90762 [link](https://github.com/AlexeySorokin/GramEval2020) [Sorokin, Smurov, Kirianov 2020](http://www.dialog-21.ru/media/5118/sorokinaaplusetal-162.pdf)
2. lima - 0.87870 [link](https://github.com/aymara/lima/tree/grameval-2020) [Bocharov, de Chalendar 2020](http://www.dialog-21.ru/media/5075/bocharovvvplusdechalendarg-158.pdf)
2. vocative - 0.85198 [link - tagger](https://github.com/Koziev/rupostagger2) [link - lemmatizer](https://github.com/Koziev/rulemma)
2. baseline - 0.80377 [link](https://github.com/dialogue-evaluation/GramEval2020/tree/master/baseline)

### Competition description
We invite you to participate in the GramEval-2020 shared task. During the shared task, participants build systems that identify: 
 - Morphological characteristics of the word (part of speech and features), 
 - Lemma of the word
 - Syntactic relations (dependencies) 
 
 A cumulative evaluation score is computed on all tokens taking into account:
  - POS (part of speech) accuracy
  - morphological features accuracy
  - LAS accuracy (labeled attachment score for dependency relations)
  - lemmatization accuracy
 
See the performance of publicly available tools for Russian - [analysis by Igor Trofimov](https://github.com/dialogue-evaluation/GramEval2020/blob/master/eval_it.pdf)

All metrics are calculated by the [evaluate.py](https://github.com/dialogue-evaluation/GramEval2020/blob/master/evaluate.py) script. 

### Motivation: 
We believe that multi-level language structures need to be labeled together, otherwise errors in one tag level lead to errors in the following. 
Existing pipelines “tokenization - morphology - lemmatization - syntax” accumulate errors in each stage.  

We welcome systems that perform equally well on Russian tests of different registers (including texts that differ in style, scope and genre, region, time of creation), register-specific words and constructions.  

### Objective: 
We encourage participants to build systems that implement full morphological and syntactic annotation and lemmatization within the framework of [Universal Dependencies](http://universaldependencies.org/) (UD). It is allowed that your system would build upon the baseline pipeline or use components of other existing open decisions. 

### Data: 
Training data include news, social networks, fiction and non-fiction, business, poetry, and historical texts of the 17th century. 
Data listed in [data.md](https://github.com/dialogue-evaluation/GramEval2020/blob/master/data.md) file include: 
* training data with full annotation - the resulting work of our team of annotators and existing UD treebanks  
* additional data with automatic ("dirty") annotation  
* additional materials such as frequency lists and models based on the third-party resources  
* development sets ([open test data](https://github.com/dialogue-evaluation/GramEval2020/tree/master/dataOpenTest)) for preliminary evaluation of the model  

It is allowed to train on all the data (train + dev), but for the convenience of participants, the dev set is selected for the preliminary evaluation of the model. As data come from different sources, they differ in data size for different registers, available levels of annotation and annotation quality, and attested combinations of feature tags for particular parts of speech.     

During the evaluation phase, submissions are evaluated against the closed test data, which include texts in many genres and from different sources in Russian.  

### Data format: 
Universal Dependencies standard, in the CONLL-U format, see [data.md](https://github.com/dialogue-evaluation/GramEval2020/blob/master/data.md). UD tagset for Russian is available [here](https://github.com/dialogue-evaluation/GramEval2020/tree/master/UDtagset).  

### Baselines: 
#### Morphology:
RnnMorph (winner of MorphoRuEval 2017)

#### Syntax:
Udpipe (baseline CONLL 2018)

See the [baseline](https://github.com/dialogue-evaluation/GramEval2020/tree/master/baseline). 

## Paper Submission 
 - Paper due - March 18 
 - Статьи должны быть загружены на платформу [link](https://cmt3.research.microsoft.com/User/Login?ReturnUrl=%2FDIALOGUE2020%2F) в раздел Основная сессия (Substantive session). 
  - Для организации рецензирования оргкомитет Диалога просит до 10 марта загрузить название статьи и ее краткое резюме в систему.

Поданные анонимизированные тексты проходят стандартную процедуру двойного слепого рецензирования конференции Диалог с участием организаторов GramEval2020. Место системы в рейтинге не является решающим критерием для рецензентов. Оценивается в первую очередь ясность изложения информации об использованных методах, архитектурах и данных, а также насколько статья интересна для широкой аудитории. Рекомендуем включить в статью разбор итоговых и промежуточных результатов вашей системы, дополнительные метрики оценки качества, а также обсуждение дискуссионных моментов с точки зрения общего развития отрасли. По результатам рецензирования будет принято решение о публикации статьи в основном сборнике (индексируется SCOPUS) или в качестве онлайн-публикации на сайте Диалога (такая судьба ждет сухие технические отчеты). 

### Important Dates: 
 - February 1, 2020 - the release of gold and additional "dirty" training data obtained using automatic marking 
 - February 15, 2020 - testing systems 
 - February 23-24, 2020 - final submission 
 - March 5, 2020 - announcement of the results

We are open to questions about data, metrics, and testing procedures. 
email: grameval2020@gmail.com 
telegram: t.me/grameval2020 

Sincerely, 
Competition Committee
