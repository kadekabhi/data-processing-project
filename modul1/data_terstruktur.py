import pandas as pd

data = {
    'ID_Pelanggan':[101,102,103,104],
    'Nama':['Budi','Siti','Joko','Ani'],
    'Usia':[25,30,22,28]
}
df = pd.DataFrame(data)

print("DataFrame yang dibuat:")
print(df)

df.to_csv('data_pelanggan.csv', index=False)
print("\nDataFrame berhasil disimpan ke 'data_pelanggan.csv'")

df_baru = pd.read_csv('data_pelanggan.csv')
print("\nDataFrame yang dimuat dari CSV:")
print(df_baru)

print("\nInformasi DataFrame:")
df_baru.info()
print("\nRinkasan statistik:")
print(df_baru.describe())

import matplotlib.pyplot as plt

# Rata-rata usia
print("\nRata-rata usia pelanggan:", df_baru['Usia'].mean())

# Pelanggan tertua
print("Pelanggan tertua:")
print(df_baru.loc[df_baru['Usia'].idxmax()])

# Visualisasi distribusi usia
plt.hist(df_baru['Usia'])
plt.title("Distribusi Usia Pelanggan")
plt.xlabel("Usia")
plt.ylabel("Jumlah")
plt.show()