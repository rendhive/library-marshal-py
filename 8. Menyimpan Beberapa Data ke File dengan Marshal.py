import marshal

data1 = {'key1': 'value1'}
data2 = {'key2': 'value2'}

with open('multiple_data.marshal', 'wb') as file:
    marshal.dump(data1, file)
    marshal.dump(data2, file)

print("Beberapa data berhasil diserialisasi ke 'multiple_data.marshal'.")
# Fungsi: Menyimpan beberapa objek ke dalam file menggunakan marshal.
# Kondisi: Ketika Anda ingin menyimpan lebih dari satu objek dalam satu file.
