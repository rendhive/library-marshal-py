import marshal

data = []

with open('multiple_data.marshal', 'rb') as file:
    while True:
        try:
            data.append(marshal.load(file))
        except EOFError:
            break

print("Data yang dibaca dari 'multiple_data.marshal':", data)
# Fungsi: Membaca beberapa objek dari file yang telah diserialisasi.
# Kondisi: Ketika Anda ingin memulihkan semua objek dari satu file.
