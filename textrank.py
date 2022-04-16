'''
A classificação de texto é uma técnica de sumarização 
baseada em gráfico com extrações de palavras-chave do documento. 
'''

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

f = open("./texto3.txt", "r")
#f = open("./texto.txt", "r")
sentence = f.read()
#sentence = '''O que a mídia não mostra é que nenhum outro para nenhum outro representante Líder mundial no G20 na Itália pela recepção que o bolsonaro teve Gente onde o cara vai ele arrasta Multidões aí ver a Globo bolsonaro isolado isolado por quem até Angela Merkel chama bolsonaro para mim. Vamos conversar e assim a gente tem uma imagem tão distorcida e tão ruim tão negacionismo do que é o Brasil, porque hoje é necessário estar muito ruim. Você não dorme já disse isso que quando o bolsonaro ganhou toda a oposição se colocou dentro tivamente contra ele, porque se o cara sai daí ele vai ser eleito de novo. A gente se falou.O que o bolsonaro fala assim? Nossa água e escovar o dente é bom aí vai aparecer alguém falando. Olha, eu acho que escovar o dente não é uma boa ideia. Olha nós specialists vão achar especialistas para te convencer que escovar o dente pode não ser uma boa ideia porque tudo que o cara fala é ruim simplesmente porque nada de bom pode vir dele que ele é o símbolo do mal, só que onde ele ele arrasta Multidões Multidões, gente, olha a galera que tava lá na Itália está no mito isso é espontâneo e ser Genuíno, qual outro qual outro líder da recepção Gente ninguém fez bolsonaro sozinho, ele tem mais seguidores na internet do que todos os concorrentes de juntos todos juntos, não dá um bolsonaro.Então assim é pânico, ele vai noticiar que ele foi lá conversou com seu tedros adhanom. Graças a Deus eu estava sem máscara, né, Mário, mas coisas importantes são deixadas de lado. Por que não se pode falar de coisas importantes do Governo está falando isso que o Governo está fazendo isso não é só ir na Itália não, gente. Isso é o que acontece aqui ninguém deu repercussão nenhuma para o leilão do Tarcísio lá quebrando na tela lá, tô maior leilão, ninguém tá falando das ferrovias para o Pacheco tá sentado em cima e a gente já vai falar contigo tá parceiro, já vai falar de você, mas isso acontece porque hoje é necessário se colocar ultimamente contra o governo. Seja lá com relação ao que for e eu não acho que ele foi passou vergonha na Itália. Eu acho que ele deixou ele quem viu viu confiando que o olho viu.Chegou em casa estava na minhas redes sociais a multidão esperando o presidente e está sozinho isolado com todo mundo. Olha lá galera gritando Lula livre não dá mais para que os seus olhos não veem. Isso é um problema gente porque nós temos uma mídia imensa em abstinência que quer te convencer do contrário.'''

parser = PlaintextParser.from_string(sentence, Tokenizer('portuguese'))
#parser = PlaintextParser.from_string(string=sentence, tokenizer=Tokenizer('portuguese'))

#parser = PlaintextParser.from_file("./texto.txt", Tokenizer('portuguese'))
summarizer = TextRankSummarizer()
qtd_sentencas = 1 # 1 = a frase mais importante
summary = summarizer(parser.document, qtd_sentencas)

frase_final = ''
for sentence in summary:
    #print(' << TextRank >> ')
    frase_final += '... ' + str(sentence)
    #print(sentence)

print(frase_final[3:])