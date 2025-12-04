import marshal

try:
    with open('non_existing_file.marshal', 'rb') as file:
        data = marshal.load(file)
except FileNotFoundError:
    print("File tidak ditemukan.")
# Fungsi: Menangani error saat mencoba memuat objek dari file.
# Kondisi: Saat Anda ingin memastikan aplikasi Anda tidak berhenti jika file tidak ada.
