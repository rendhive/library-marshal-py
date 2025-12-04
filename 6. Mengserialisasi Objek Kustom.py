import marshal

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)

with open('person.marshal', 'wb') as file:
    marshal.dump(person, file)

print("Objek 'Person' berhasil diserialisasi ke 'person.marshal'.")
# Fungsi: Menyimpan objek kustom (mis. kelas pengguna) ke dalam file.
# Kondisi: Ketika Anda memiliki objek kustom yang ingin disimpan untuk penggunaan di masa mendatang.
