import nltk

nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

#f = open("./texto.txt", "r")
#sentence = f.read()

sentence = '''O que a mídia não mostra é que nenhum outro para nenhum outro representante Líder mundial no G20 na Itália pela recepção que o bolsonaro teve Gente onde o cara vai ele arrasta Multidões aí ver a Globo bolsonaro isolado isolado por quem até Angela Merkel chama bolsonaro para mim. Vamos conversar e assim a gente tem uma imagem tão distorcida e tão ruim tão negacionismo do que é o Brasil, porque hoje é necessário estar muito ruim. Você não dorme já disse isso que quando o bolsonaro ganhou toda a oposição se colocou dentro tivamente contra ele, porque se o cara sai daí ele vai ser eleito de novo. A gente se falou.O que o bolsonaro fala assim? Nossa água e escovar o dente é bom aí vai aparecer alguém falando. Olha, eu acho que escovar o dente não é uma boa ideia. Olha nós specialists vão achar especialistas para te convencer que escovar o dente pode não ser uma boa ideia porque tudo que o cara fala é ruim simplesmente porque nada de bom pode vir dele que ele é o símbolo do mal, só que onde ele ele arrasta Multidões Multidões, gente, olha a galera que tava lá na Itália está no mito isso é espontâneo e ser Genuíno, qual outro qual outro líder da recepção Gente ninguém fez bolsonaro sozinho, ele tem mais seguidores na internet do que todos os concorrentes de juntos todos juntos, não dá um bolsonaro.Então assim é pânico, ele vai noticiar que ele foi lá conversou com seu tedros adhanom. Graças a Deus eu estava sem máscara, né, Mário, mas coisas importantes são deixadas de lado. Por que não se pode falar de coisas importantes do Governo está falando isso que o Governo está fazendo isso não é só ir na Itália não, gente. Isso é o que acontece aqui ninguém deu repercussão nenhuma para o leilão do Tarcísio lá quebrando na tela lá, tô maior leilão, ninguém tá falando das ferrovias para o Pacheco tá sentado em cima e a gente já vai falar contigo tá parceiro, já vai falar de você, mas isso acontece porque hoje é necessário se colocar ultimamente contra o governo. Seja lá com relação ao que for e eu não acho que ele foi passou vergonha na Itália. Eu acho que ele deixou ele quem viu viu confiando que o olho viu.Chegou em casa estava na minhas redes sociais a multidão esperando o presidente e está sozinho isolado com todo mundo. Olha lá galera gritando Lula livre não dá mais para que os seus olhos não veem. Isso é um problema gente porque nós temos uma mídia imensa em abstinência que quer te convencer do contrário.'''

tokenizer = nltk.RegexpTokenizer(r"\w+") # remove pontuação
oritxt = tokenizer.tokenize(sentence) # remove pontuação
t1 = ' '.join(oritxt)
text = t1.lower()

tokenized_text = nltk.word_tokenize(text)
stopwords = nltk.corpus.stopwords.words('portuguese')
word_freq = nltk.FreqDist(tokenized_text)
dict_filter = lambda word_freq, stopwords: dict( (word,word_freq[word]) for word in word_freq if word not in stopwords )
filtered_word_freq = dict_filter(word_freq, stopwords)

sort_orders = sorted(filtered_word_freq.items(), key=lambda x: x[1], reverse=True)
primeiras_cinco = {}
cont=0
for i in sort_orders:
    cont += 1
    #print(i[0], i[1])
    if(cont < 6):
        primeiras_cinco[i[0]] = i[1]
    if(cont == 6):
        break

print(primeiras_cinco)
print(list(primeiras_cinco.keys())[0])
