'''
o aprimoramento do método de Luhn mencionado anteriormente. 
Edmundson adicionou mais 3 heurísticas ao método para medir a importância das sentenças. 
Ele encontra as chamadas palavras pragmáticas, as palavras que estão nos cabeçalhos e a posição dos termos extraídos. 
Portanto, este método possui 4 sub-métodos e a combinação adequada deles resulta no método de Edmundson.
'''
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
#from sumy.summarizers.text_rank import TextRankSummarizer

from sumy.summarizers.edmundson import EdmundsonSummarizer

import nltk
stopwords = nltk.corpus.stopwords.words('portuguese')

parser = PlaintextParser.from_file("./texto.txt", Tokenizer('portuguese'))
summarizer = EdmundsonSummarizer()
summarizer.bonus_words = ['politica'] # positively relevant
summarizer.stigma_words = ['STF'] # negatively relevant.
summarizer.null_words = stopwords # irrelevant words
qtd_sentencas = 2 # 1 = a frase mais importante
summary = summarizer(parser.document, qtd_sentencas)

for sentence in summary:
    print(' << EdmundsonSummarizer >> ')
    print(sentence)