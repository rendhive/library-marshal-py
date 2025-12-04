import marshal

with open('data.marshal', 'rb') as file:
    loaded_data = marshal.load(file)

print("Tipe dari loaded_data:", type(loaded_data))
# Fungsi: Memeriksa tipe objek setelah deserialisasi.
# Kondisi: Ketika Anda ingin memastikan objek yang dimuat dari file sudah sesuai yang diharapkan.
