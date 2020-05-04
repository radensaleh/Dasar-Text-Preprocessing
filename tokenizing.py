# library python
import string
from nltk.tokenize import word_tokenize, sent_tokenize

# memisahkan kalimat menjadi kata-kata + case folding
kalimat1 = "Saya adalah TOP 21 Alucard, MMR saya 1843."
kalimat1 = kalimat1.translate(str.maketrans('','',string.punctuation)).lower()
word_tokens = word_tokenize(kalimat1)
print(word_tokens)

# memisahkan kalimat pada paragraf (.)
kalimat2 = "Andi kerap melakukan transaksi rutin secara daring atau online. Menurut Andi belanja online lebih praktis & murah."
sent_tokens = sent_tokenize(kalimat2)
print(sent_tokens)
