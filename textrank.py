'''
A classificação de texto é uma técnica de sumarização 
baseada em gráfico com extrações de palavras-chave do documento. 
'''

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

parser = PlaintextParser.from_file("./texto.txt", Tokenizer('portuguese'))
summarizer = TextRankSummarizer()
qtd_sentencas = 2 # 1 = a frase mais importante
summary = summarizer(parser.document, qtd_sentencas)

frase_final = ''
for sentence in summary:
    #print(' << TextRank >> ')
    frase_final += '... ' + str(sentence)
    #print(sentence)

print(frase_final[3:])