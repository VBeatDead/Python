buku_tersedia = {
    'BK1': 'Si Kancil',
    'BK2': 'Putri Bangun Tidur',
    'BK3': 'Adit Sopo Jarwo',
    'BK4': 'Perahu Kertas',
    'BK5': 'Si Udin Bertanya',
}

peminjaman = {}

def tampilkan_buku_tersedia():
    print("Buku Tersedia:")
    for kode, judul in buku_tersedia.items():
        print(f"{kode}: {judul}")

def tambah_buku():
    kode = input("Masukkan kode buku: ")
    judul = input("Masukkan judul buku: ")
    buku_tersedia[kode] = judul
    print(f"Buku '{judul}' dengan kode '{kode}' telah ditambahkan.")

def pinjam_buku(username):
    tampilkan_buku_tersedia()
    kode = input("Masukkan kode buku yang ingin Anda pinjam: ")
    
    if kode in buku_tersedia:
        if kode not in peminjaman:
            peminjaman[kode] = username
            print(f"Buku '{buku_tersedia[kode]}' berhasil dipinjam oleh {username}.")
        else:
            print(f"Buku '{buku_tersedia[kode]}' sudah dipinjam oleh {peminjaman[kode]}.")
    else:
        print("Buku dengan kode tersebut tidak tersedia.")

def kembalikan_buku(username):
    kode = input("Masukkan kode buku yang ingin Anda kembalikan: ")
    
    if kode in peminjaman and peminjaman[kode] == username:
        del peminjaman[kode]
        print(f"Buku '{buku_tersedia[kode]}' telah dikembalikan oleh {username}.")
    else:
        print("Anda tidak dapat mengembalikan buku ini atau buku tidak dipinjam oleh Anda.")

def main():
    while True:
        print("\nSelamat datang")
        print("1. Login sebagai admin")
        print("2. Login sebagai user")
        print("3. Keluar")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            # Admin login
            password = input("Masukkan password admin: ")
            if password == "admin123":
                tambah_buku()
            else:
                print("Password admin salah.")

        elif pilihan == '2':
            # User login
            username = input("Masukkan username: ")
            while True:
                print("\nMenu User:")
                print("1. Tampilkan buku tersedia")
                print("2. Pinjam buku")
                print("3. Kembalikan buku")
                print("4. Logout")
                user_pilihan = input("Pilih opsi: ")

                if user_pilihan == '1':
                    tampilkan_buku_tersedia()

                elif user_pilihan == '2':
                    pinjam_buku(username)

                elif user_pilihan == '3':
                    kembalikan_buku(username)

                elif user_pilihan == '4':
                    break
                else:
                    print("Pilihan tidak valid.")

        elif pilihan == '3':
            print("Terima kasih telah menggunakan layanan perpustakaan.")
            break

        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()