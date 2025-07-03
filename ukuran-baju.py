kode_baju = input("Masukkan Kode Baju [SP / AD] : ").upper()
ukuran = input("Masukkan Ukuran[S / M] : ").upper()

if kode_baju == "SP":
    merk = "SuperDry"
    if ukuran == "S":
        harga = 450000
    elif ukuran == "M":
        harga = 500000
    else:
        harga = 0
elif kode_baju == "AD":
    merk = "Adidas"
    if ukuran == "S":
        harga = 650000
    elif ukuran == "M":
        harga = 700000
    else:
        harga = 0
else:
    merk = "Anda Salah Input Kode Merk"
    harga = 0

print("===========================")
print(f"Merk Baju : {merk}")
print(f"Harga Baju : Rp.{harga}")