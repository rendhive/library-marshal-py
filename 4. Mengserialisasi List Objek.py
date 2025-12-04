import marshal

data_list = [1, 2, 3, {'a': 'A', 'b': 'B'}]

with open('list_data.marshal', 'wb') as file:
    marshal.dump(data_list, file)

print("List berhasil diserialisasi dan disimpan ke 'list_data.marshal'.")
# Fungsi: Menyimpan list (atau koleksi) objek Python ke dalam file.
# Kondisi: Ketika Anda ingin menyimpan koleksi objek untuk diproses kemudian.
