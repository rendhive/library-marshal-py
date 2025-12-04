import marshal

with open('text_data.marshal', 'rb') as file:
    read_text = marshal.load(file)

print("Teks yang dibaca dari file:", read_text)
# Fungsi: Membaca dan mendeserialisasi data teks dari file.
# Kondisi: Ketika Anda ingin memulihkan data teks yang tersimpan.
