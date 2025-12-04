import marshal

text_data = "Ini adalah teks yang akan disimpan."
with open('text_data.marshal', 'wb') as file:
    marshal.dump(text_data, file)

print("Teks berhasil disimpan ke 'text_data.marshal'.")
# Fungsi: Menyimpan string atau data teks ke file menggunakan marshal.
# Kondisi: Ketika Anda ingin menyimpan teks langsung ke file dalam format yang lebih efisien.
