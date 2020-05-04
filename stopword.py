from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string

kalimat = "Andi kerap melakukan transaksi rutin secara daring atau online. Menurut Andi belanja online lebih praktis & murah."
kalimat = kalimat.translate(str.maketrans('','',string.punctuation)).lower()

tokens = word_tokenize(kalimat)
listStopwords = set(stopwords.words('indonesian'))

removed = []
for t in tokens:
    if t not in listStopwords:
        removed.append(t)

print(removed)