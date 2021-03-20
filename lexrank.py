'''
 A ideia principal do LexRank é que as frases “recomendem” outras frases semelhantes ao leitor. 
 Portanto, se uma frase for muito semelhante a muitas outras, 
 provavelmente será uma frase de grande importância
'''
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer 

parser = PlaintextParser.from_file("texto.txt", Tokenizer('portuguese'))
summarizer = LexRankSummarizer()
summary = summarizer(parser.document, 1)

for sentence in summary:
    print(' << lex rank >> ')
    print(sentence)