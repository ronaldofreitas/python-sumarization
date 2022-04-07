import nltk

f = open("./texto-2.txt", "r")
sentence = f.read()

tokenizer = nltk.RegexpTokenizer(r"\w+")

oritxt = tokenizer.tokenize(sentence)


t1 = ' '.join(oritxt)
text = t1.lower()
print('**************************')
#text = '''vamos tentar contar as palavras mais usadas e vamos também vencer'''

#nltk.download('stopwords')
#stopwords = nltk.corpus.stopwords.words('portuguese')
#print(len(stopwords))


#text = "Hello, this is my sentence. It is a very basic sentence with not much information in it"
tokenized_text = nltk.word_tokenize(text)
stopwords = nltk.corpus.stopwords.words('portuguese')
word_freq = nltk.FreqDist(tokenized_text)
dict_filter = lambda word_freq, stopwords: dict( (word,word_freq[word]) for word in word_freq if word not in stopwords )
filtered_word_freq = dict_filter(word_freq, stopwords)


#print(filtered_word_freq)

sort_orders = sorted(filtered_word_freq.items(), key=lambda x: x[1], reverse=True)
primeiras_cinco = {}
cont=0
for i in sort_orders:
    cont += 1
    print(i[0], i[1])
    if(cont < 6):
        primeiras_cinco[i[0]] = i[1]
        #print(i[0], i[1])
    if(cont == 6):
        break

print(primeiras_cinco)
print(list(primeiras_cinco.keys())[0])
