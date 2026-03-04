from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline  import make_pipeline

data_latihan = [
    ("Promo diskon besar, beli sekarang!", "spam"),
    ("Rapat proyek besok jam 10 pagi.", "bukan_spam"),
    ("Menangkan hadiah undian gratis!", "spam"),
    ("Tolong kirimkan laporan penjualan.", "bukan_spam"),
    ("Voucher spesial hanya untukmu.", "spam")
]

teks_latihan = [item[0] for item in data_latihan]
label_latihan = [item[1] for item in data_latihan]

model = make_pipeline(TfidfVectorizer(), MultinomialNB())

model.fit(teks_latihan, label_latihan)

teks_baru = ["Promo unndian berhadiah motor, klik disini!"]

prediksi = model.predict(teks_baru)

print(f"## 1. Hasil klasifikasi teks ##")
print(f"Teks: '{teks_baru[0]}'")
print(f"Prediksi kategori: {prediksi[0]}")
print("-" * 30)