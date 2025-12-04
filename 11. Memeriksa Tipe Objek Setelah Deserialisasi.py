import marshal

data = {'key': 'value'}

# Serialisasi dan kemudian deserialisasi
with open('data.marshal', 'wb') as file:
    marshal.dump(data, file)

with open('data.marshal', 'rb') as file:
    loaded_data = marshal.load(file)

print("Tipe dari loaded_data:", type(loaded_data))
# Fungsi: Memverifikasi tipe objek setelah deserialisasi.
# Kondisi: Ketika Anda perlu memastikan bahwa objek yang dimuat adalah dari tipe yang diharapkan.
