import marshal

with open('data.marshal', 'rb') as file:
    loaded_data = marshal.load(file)

print("Data yang dimuat:", loaded_data)
# Fungsi: Menampilkan data yang dimuat dari file.
# Kondisi: Ketika Anda ingin memverifikasi data yang telah disimpan.
