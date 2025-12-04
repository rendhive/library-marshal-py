import marshal

# Menggabungkan beberapa objek menjadi satu struktur besar
complex_data = {
    'people': [
        {'name': 'Tom', 'age': 28},
        {'name': 'Sara', 'age': 32}
    ],
    'company': 'TechCorp'
}

with open('complex_structure.marshal', 'wb') as file:
    marshal.dump(complex_data, file)

print("Data kompleks berhasil diserialisasi ke 'complex_structure.marshal'.")
# Fungsi: Menyimpan struktur data yang kompleks ke dalam file marshal.
# Kondisi: Ketika Anda ingin menyimpan data dengan hierarki yang lebih rumit.
