total_belanja = 0

print("=== PROGRAM KASIR MINI MARKET ===")
print("Input angka 0 jika barang sudah selesai dihitung.\n")

while True:
    # Mengambil input dari kasir (diubah ke integer/angka)
    harga = int(input("Masukkan harga barang (Rp): "))
    
    # Kondisi berhenti: jika harga yang dimasukkan adalah 0
    if harga == 0:
        print("Menghitung total...")
        break  # Keluar paksa dari loop while True
        
    # Jika bukan 0, tambahkan harga barang ke total belanja
    total_belanja += harga

if total_belanja > 100000:
    total_belanja *= 0.9

print(f"Total yang harus dibayar pelanggan: Rp {total_belanja}")
print("Terima kasih!")