import marshal

data = {'key': 'value', 'number': 100}

with open('strong_data.marshal', 'wb') as file:
    marshal.dump(data, file)

print("Data kuat berhasil diserialisasi ke 'strong_data.marshal'.")
# Fungsi: Menyimpan data yang lebih kompleks ke dalam file.
# Kondisi: Ketika Anda bekerja dengan objek penanganan data yang kompleks.
