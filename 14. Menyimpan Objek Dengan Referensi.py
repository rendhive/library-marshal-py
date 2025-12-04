import marshal

data = {'a': 1, 'b': 2}
data['c'] = data  # Referensi kepada objek yang sama

with open('reference_data.marshal', 'wb') as file:
    marshal.dump(data, file)

print("Data dengan referensi berhasil diserialisasi ke 'reference_data.marshal'.")
# Fungsi: Menyimpan objek dengan referensi di dalam file.
# Kondisi: Ketika objek memiliki referensi kepada dirinya sendiri.
