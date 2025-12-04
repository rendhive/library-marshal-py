import marshal

data = {'key': 'value'}

with open('data_v3.marshal', 'wb') as file:
    marshal.dump(data, file, 3)  # Menggunakan protokol versi 3

print("Data berhasil disimpan dengan protokol versi 3 ke 'data_v3.marshal'.")
# Fungsi: Menggunakan protokol marshaling spesifik.
# Kondisi: Ketika Anda ingin memastikan bahwa data menggunakan versi tertentu untuk kompatibilitas.
