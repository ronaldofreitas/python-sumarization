'''
É um dos primeiros algoritmos sugeridos pelo famoso pesquisador da IBM 
que lhe deu o nome. Ele pontua as sentenças com base na frequência das palavras mais importantes. 
'''

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer

parser = PlaintextParser.from_file("texto.txt", Tokenizer('portuguese'))
#parser = PlaintextParser.from_string(txt, Tokenizer('portuguese'))

sumarizador = LuhnSummarizer()

resumo = sumarizador(parser.document, 1)

for sentence in resumo:
    print(' << LUHN >> ')
    print(sentence)