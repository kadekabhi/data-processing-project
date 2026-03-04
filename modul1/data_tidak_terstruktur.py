import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

kalimat = "buku ini sangat BAGUS sekali, saya sangat suka !"

kalimat_lower = kalimat.lower()
print("setelah case folding:", kalimat_lower)


tokens = word_tokenize(kalimat_lower)
print("hasil tokenasasi:", tokens)

tokens_bersih = [token for token in tokens if token.isalpha()]
print("Setelah menghilangkan tanda  baca:", tokens_bersih)

stop_words = set(stopwords.words('indonesian'))
filtered_tokens = [word for word in tokens_bersih if word not in stop_words]
print("Setelah menghilangkan stop words:", filtered_tokens)

from collections import Counter

word_freq = Counter(filtered_tokens)
print("\nFrekuensi kata:", word_freq)