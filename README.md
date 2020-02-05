# GramEval-2020

## A shared task on full morphology and dependency parsing of Russian texts 

[Codalab Link](https://competitions.codalab.org/competitions/22902?secret_key=38f3cda8-d1c4-427b-ba06-23ba44ff2264)
Join our discussion group in Telegram: [@grameval2020](http://t.me/grameval2020) 

We invite you to participate in the GramEval-2020 shared task. During the shared task, participants build systems that identify: 
 - Morphological characteristics of the word (part of speech and features), 
 - Lemma of the word
 - Syntactic relations (dependencies) 
 
 A cumulative evaluation score is computed on all tokens taking into account:
  - POS (part of speech) accuracy
  - morphological features accuracy
  - LAS accuracy (labeled attachment score for dependency relations)
  - lemmatization accuracy
 
All metrics are calculated by the [evaluate.py](https://github.com/dialogue-evaluation/GramEval2020/blob/master/evaluate.py) script. 

### Motivation: 
We believe that multi-level language structures need to be labeled together, otherwise errors in one tag level lead to errors in the following. 
Existing pipelines “tokenization - morphology - lemmatization - syntax” accumulate errors in each stage.  

We welcome systems that perform equally well on Russian tests of different registers (including texts that differ in style, scope and genre, region, time of creation), register-specific words and constructions.  

### Objective: 
We encourage participants to build systems that implement full morphological and syntactic annotation and lemmatization within the framework of [Universal Dependencies](http://universaldependencies.org/) (UD).

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

It is allowed that your system would build upon the baseline pipeline or use components of other existing open decisions. 

### Important Dates: 
 - February 1, 2020 - the release of gold and additional "dirty" training data obtained using automatic marking 
 - February 15, 2020 - testing systems 
 - February 22, 2020 - final submission 
 - March 5, 2020 - announcement of the results

We are open to questions about data, metrics, and testing procedures. 
email: grameval2020@gmail.com 
telegram: t.me/grameval2020 

Sincerely, 
Competition Committee
