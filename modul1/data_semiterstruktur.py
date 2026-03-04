import json
json_string = '''
{
    "produk": "Laptop A",
    "harga": 1500000,
    "spesifikasi": {
      "prosesor": "intel i7",
      "RAM": "16 GB"
      },
    "ulasan": [
      {"pengguna": "Budi", "rating": 5, "komentar": "sangat bagus"},
      {"pengguna": "Siti", "rating": 4, "komentar": "Lumayan"}
      ]
}
'''
data_json = json.loads(json_string)

print("Data Json yang dimuat:")
print(data_json)

print("\nNama produk:", data_json['harga'])
print("Harga", data_json['harga'])

print("Prosesor:", data_json['spesifikasi']['prosesor'])

print("\nKomentar dari pengguna pertama:", data_json['ulasan'][0]['komentar'])

ratings = [ulasan['rating'] for ulasan in data_json['ulasan']]
print("\nRata-rata rating:", sum(ratings) / len(ratings))