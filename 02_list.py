# Belajar List - koleksi data yang bisa diubah

gunung = ["Semeru", "Bromo", "Arjuno", "Welirang"]

# Akses elemen
print(gunung[0])        # Semeru (index mulai dari 0)
print(gunung[-1])       # Welirang (index terakhir)

# Tambah elemen
gunung.append("Ijen")
print(gunung)

# Hapus elemen
gunung.remove("Bromo")
print(gunung)

# Loop through list
for g in gunung:
    print(f"Gunung: {g}")