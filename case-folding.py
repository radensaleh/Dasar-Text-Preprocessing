# library python
import string
import re

# mengubah kata ke dalam huruf kecil
kalimat1 = "Nama Saya Raden, Saya Seorang programmEr dari CIREBON. Saat ini saya sedang menempuh Pendidikan Diploma 4 di Politeknik NEGERI Indramayu Program Studi D4 Rekayasa Perangkat Lunak, saya anak pertama Dari 2 bersaudara."
lower_case = kalimat1.lower()
print('Lower Case : ' + lower_case)

# menghapus kata dari tanda baca
kalimat2 = "Ini &adalah [contoh] kalimat? {dengan} tanda. baca?!!"
trans = kalimat2.translate(str.maketrans('', '', string.punctuation))
print('Punctuation : ' + trans)

# menghapus karakter kosong diawal dan diakhir
kalimat3 = "      ini contoh kalimatnyaa   \t    "
whitespace = kalimat3.strip()
print('Whitespace : ' + whitespace)

# menghapus angka
kalimat4 = "Saya adalah TOP 21 Alucard, MMR saya 1843"
ree = re.sub(r"\d+", "", kalimat4)
print('Re : ' + ree)