def cetak_segitiga_siku(tinggi):
    for i in range(1, tinggi + 1):
        print('*' * i)

def cetak_persegi_panjang(panjang, lebar):
    for i in range(lebar):
        print('*' * panjang)

def cetak_belah_ketupat(tinggi):
    for i in range(1, tinggi +1):
        print (' ' * (tinggi - i) + '*' * (2 * i -1))
    for i in range(tinggi - 1, 0, -1):
        print (' ' * (tinggi - i) + '*' * (2 * i -1))

def cetak_segitiga_terbalik(tinggi):
    for i in range(tinggi, 0, -1):
        print (' ' * (tinggi - i) + '*' * (2 * i -1))

def cetak_jam_pasir(tinggi):
    for i in range(tinggi, 0, -1):
        print(' ' * (tinggi -i) + '*' * (2 * i -1))
    for i in range(2, tinggi + 1):
        print(' ' * (tinggi -i) + '*' * (2 * i -1))
def main():
    print("PILIH BANGUN DATAR:")
    print("1. Segitiga siku-siku")
    print("2. Persegi panjang")
    print("3. Belah ketupat")
    print("4. Segitiga terbalik")
    print("5. Jam pasir")

    pilihan = input("Masukkan nomor pilihan anda: ")

    if pilihan == '1':
        tinggi = int(input ("Masukan tinggi segitiga:"))
        cetak_segitiga_siku(tinggi)
    elif pilihan == '2':
        panjang = int(input("Masukkan panjang persegi panjang: "))
        lebar = int(input("Masukkan lebar persegi panjang: "))
        if panjang == lebar:
            int(input("Panjang dan lebar tidak bolegh sama."))
        else:
            cetak_persegi_panjang(panjang, lebar)
    elif pilihan == '3':
        tinggi = int(input("Masukan tinggi belahketupat: "))
        cetak_belah_ketupat(tinggi)
    elif pilihan == '4':
        tinggi = int(input("Masukan tinggi segitiga terbalik: "))
        cetak_segitiga_terbalik(tinggi)
    elif pilihan == '5':
        tinggi = int(input("Masukan tinggi jam pasir: "))
        cetak_jam_pasir(tinggi)
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()