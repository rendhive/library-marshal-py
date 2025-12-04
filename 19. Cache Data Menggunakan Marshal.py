import marshal

cache_data = {'item1': 'apple', 'item2': 'banana'}

with open('cache_data.marshal', 'wb') as file:
    marshal.dump(cache_data, file)

print("Data cache berhasil disimpan ke 'cache_data.marshal'.")
# Fungsi: Menyimpan data cache ke dalam file agar dapat digunakan kembali.
# Kondisi: Ketika Anda ingin mempercepat proses dengan menyimpan data yang sering digunakan.
