from textblob import TextBlob

ulasan_positif = "Baterai ponsel ini awet banget, kameranya juga bagus!"
ulasan_negatif = "Sangat mengecewakan, barang rusak saat diterima."
ulasan_netral = "Paket pengirim sudah sampai."

blob_positif = TextBlob(ulasan_positif)
blob_negatif = TextBlob(ulasan_negatif)
blob_netral = TextBlob(ulasan_netral)

print(f"## 3. Hasil Analisis Sentiment ##")
print(f"Ulasan: '{ulasan_positif}'")
print(f"Polarity: {blob_positif.sentiment.polarity:.2f} -> Positif")
print("---")
print(f"Ulasan: '{ulasan_negatif}'")
print(f"Polarity: {blob_negatif.sentiment.polarity:.2f} -> Negatif")
print("---")
print(f"Ulasan: '{ulasan_netral}'")
print(f"Polarity: {blob_netral.sentiment.polarity:.2f} -> Netral")
print("---" * 30)