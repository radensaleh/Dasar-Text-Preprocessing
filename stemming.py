from nltk.stem import PorterStemmer

# proses menghilangkan infleksi kata ke bentuk dasarnya
# belum support untuk bahasa indonesia
ps = PorterStemmer()
kata = ["program", "programs", "programer", "programing", "programers"]

for k in kata:
    print(k, " : ", ps.stem(k))
