import marshal

with open('data.marshal', 'rb') as file:
    data = marshal.load(file)

print("Data yang dibaca dari 'data.marshal':", data)
# Fungsi: Membaca dan mendeserialisasi objek dari file.
# Kondisi: Ketika Anda ingin memuat kembali objek yang disimpan sebelumnya.
