buku_telepon = {
    "Andi": "0812-3456-7890",
    "Budi": "0857-1122-3344",
    "Cici": "0899-8877-6655"
}

nama = input("Masukkan nama: ")
if nama in buku_telepon:
    print(f"Nomor telepon {nama} adalah {buku_telepon[nama]}")
else:
    print(f"{nama} tidak ditemukan dalam buku telepon.")