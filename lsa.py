'''
A análise semântica latente é um método não supervisionado de sumarização 
que combina técnicas de frequência de termo com decomposição de valor singular 
para resumir textos. É uma das técnicas mais recentes sugeridas para veranização 
'''
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

parser = PlaintextParser.from_file("texto.txt", Tokenizer('portuguese'))

summarizer = LsaSummarizer()
summary =summarizer(parser.document,1)

for sentence in summary:
    print(' << LSA >> ')
    print(sentence)