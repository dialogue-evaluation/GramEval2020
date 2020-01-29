# GramEval-2020

## competition for the complete parsing of Russian texts 

Dear friends and colleagues! 
We invite you to participate in the GramEval-2020 competition. During the competition, participants aim to build systems that define: 
 - Morphological characteristics of the word (part-of-speech and full tags), 
 - Lemma of the word
 - Syntactic relations  (dependencies) 
 
 The cumulitive evaluation consists of:
  - POS tagging accuracy
  - morphological features accuracy
  - UAS accuracy (syntax)
  - lemmatization accuracy
 
 All the metrics can be found in [evaluate.py](https://github.com/dialogue-evaluation/GramEval2020/blob/master/evaluate.py)

### Motivation: 
We believe that multi-level language structures need to be labelled together, otherwise errors in one tag level will lead to errors in the following. 
Existing pipelines “tokenization - morphology - lemmatization - syntax” accumulate errors at each stage.

### Objective: 
We offer the participants to try to build systems that implement complete morphological and syntactic markup with lemmatization within the framework of Universal Dependencies.

### Data: 
On our GitHub will be posted data with full annotation - the resulting work of our team of annotators, as well as additional "dirty" data for pre-training. 

All data availaable at [data.md](https://github.com/dialogue-evaluation/GramEval2020/blob/master/data.md)

Training data includes news sources, social networks, fiction and non-fiction, business, poetry and historical texts 17th century. 
All data is divided into 2 parts - train and dev set. It is allowed to train on all the data (train + dev), but for the convenience of the participants, the dev set is selected for preliminary evaluation of the model. 
The testing procedure will include tests on “golden”  texts in many genres and from different sources in Russian. 
We welcome systems that steadily process all the variety of texts in the Russian language (including texts that differ in style, scope and genre, region, time of creation). 

### Data format: 
Universal Dependencies standard, in the CONLL-U format. 

Scripts will be published to evaluate the quality of the models for each task - we ask all participants to use them for an intermediate assessment of their models. 

### Baselines: 
#### Morphology:
RnnMorph (winner of MorphoRuEval 2017)

#### Syntax:
Udpipe (baseline CONLL 2018)

See the [baseline](https://github.com/dialogue-evaluation/GramEval2020/tree/master/baseline)

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
