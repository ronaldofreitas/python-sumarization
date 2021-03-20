'''
A classificação de texto é uma técnica de sumarização 
baseada em gráfico com extrações de palavras-chave do documento. 
'''
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

parser = PlaintextParser.from_file("texto.txt", Tokenizer('portuguese'))
summarizer = TextRankSummarizer()
summary = summarizer(parser.document, 1)

for sentence in summary:
    print(' << TextRank >> ')
    print(sentence)