from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

dokumen = [
    "Timnas sepak bola Indonesia menang telak",
    "Harga saham gabungan hari ini anjlok",
    "Pemain baru direkrut untuk liga musim depan",
    "Inflasi ekonomi menyebabkan suku bunga naik",
    "Jadwal pertandingan piala dunia diumumkan",
    "Bank sentral menaikkan suku bunga acuan"
]

vectorizer = TfidfVectorizer()
vektor_teks = vectorizer.fit_transform(dokumen)

kmeans = KMeans(n_clusters=2, random_state=0, n_init=10)
kmeans.fit(vektor_teks)

print(f"## 2. Hasil Clustering ##")
for i in range(len(dokumen)):
    print(f"Dokumen: '{dokumen[i]}'")
    print(F"Masuk ke Cluster: {kmeans.labels_[i]}")
    print("---")
print("-" * 30)