import nltk
import heapq

nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

f = open("./texto3.txt", "r")
#f = open("./texto.txt", "r")
article_text = f.read()

sentence_list = nltk.sent_tokenize(article_text)
stopwords = nltk.corpus.stopwords.words('portuguese')

word_frequencies = {}
for word in nltk.word_tokenize(article_text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

#print(word_frequencies)

sentence_scores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]

#print(sentence_scores)
#print('-----------------')
summary_sentences = heapq.nlargest(2, sentence_scores, key=sentence_scores.get)
summary = ' '.join(summary_sentences)
print(summary)
