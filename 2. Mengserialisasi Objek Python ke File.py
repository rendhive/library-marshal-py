import marshal

data = {'key': 'value', 'number': 42}

with open('data.marshal', 'wb') as file:
    marshal.dump(data, file)

print("Data berhasil diserialisasi dan disimpan ke 'data.marshal'.")
# Fungsi: Menyimpan objek Python ke dalam file menggunakan serialisasi.
# Kondisi: Ketika Anda ingin menyimpan objek Python ke disk untuk diproses kemudian.
