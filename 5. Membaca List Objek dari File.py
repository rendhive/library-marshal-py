import marshal

with open('list_data.marshal', 'rb') as file:
    data_list = marshal.load(file)

print("List yang dibaca dari 'list_data.marshal':", data_list)
# Fungsi: Membaca dan mendeserialisasi list objek dari file.
# Kondisi: Ketika Anda ingin memulihkan list objek yang tersimpan.
