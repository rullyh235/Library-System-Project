##Rully Hilman Simeon##
##Sistem Perpustakaan##

buku = {'k1' : {'Judul Buku' : 'Plutocrats', 
'Pengarang' : 'Chrystia Freeland', 'Tahun Terbit' : '2013', 'Genre' : 'economics'},
'k2' : {'Judul Buku' : 'Think and Grow Rich', 
'Pengarang' : 'Napoleon Hill', 'Tahun Terbit' : '2005', 'Genre' : 'Self Development'}}

def menu_tampil():
    print("\n=====Tampil Daftar Buku=====\n")
    print("1. Tampil Semua Daftar Buku")
    print("2. Tampil Buku Tertentu")
    print("3. Kembali ke Menu Utama")
    menu_tampil1 = input("Silahkan Pilih Sub Menu Tampil Data [1-3]: ")
    if menu_tampil1 == '1':
        tampil_semua()
    elif menu_tampil1 == '2': 
        tampil_sebagian()
    elif menu_tampil1 == '3':
        menu_utama()
    else:
        menu_tampil()

def tampil_semua():
    index = 1
    if len(buku)<=0:
        print('Data Masih Kosong')
    else:
        angka = 1
        for i in buku:
            print(f"{angka}. Kode Buku: {i}, Judul Buku: {buku[i]['Judul Buku']}, Pengarang: {buku[i]['Pengarang']}, Tahun Terbit: {buku[i]['Tahun Terbit']}, Genre: {buku[i]['Genre']}")
            angka += 1
        menu_tampil()

def tampil_sebagian():
    kodet = input("Masukan Kode Buku Yang Ingin di Tampilkan: ")
    if kodet in buku.keys():
        print(f"Kode Buku: {kodet}, Judul Buku: {buku[kodet]['Judul Buku']}, Pengarang: {buku[kodet]['Pengarang']}, Tahun Terbit: {buku[kodet]['Tahun Terbit']}, Genre: {buku[kodet]['Genre']}")
        menu_tampil()
    else:
        print("Buku Tidak Ditemukan")
    menu_tampil()

def menu_tambah():
    print("\n=======Tambah Data Perpustakaan=======\n")
    print("1. Tambah Data Buku")
    print("2. Kembali Ke Menu Utama")
    pilih = input ("Silahkan Pilih Sub Menu Tambah Data [1-2]: ")
    stat = True
    buku_baru = {}
    if pilih == '1':
        kodebuku = input("Masukan Kode Buku: ")
        if kodebuku in buku.keys():
            print("Buku Sudah Terdaftar")
        else:
            judul = input("Masukan Judul Buku: ")
            buku_baru["Judul Buku"] = judul
            pengarang = input("Masukan Pengarang Buku: ")
            buku_baru["Pengarang"] =pengarang
            tahun = input("Masukan Tahun Buku Diterbitkan: ")
            buku_baru["Tahun Terbit"] = tahun
            genre = input("Masukan Genre Buku: ")
            buku_baru["Genre"] = genre
            buku[kodebuku] = buku_baru
            print("Buku baru telah ditambahkan")
            menu_tambah()
    elif pilih == '2':
            menu_utama()
    else:
        menu_tambah()

def menu_ubah():
    print("\n=======Ubah Data Buku Perpustakan======\n")
    print("1. Ubah Data Buku")
    print("2. Kembali ke Menu Utama")
    pilih = input("Silahkan Pilih Sub Menu Ubah Data Buku [1-2]")
    if pilih == '1':
        menu_ubah1()
    elif pilih == '2':
        menu_utama()
    else:
        menu_ubah()

def menu_ubah1():
    kodet = input("Masukan Kode Buku Yang Akan Diubah: ")
    if kodet in buku.keys():
        print(f"Kode Buku: {kodet}, Judul Buku: {buku[kodet]['Judul Buku']}, Pengarang: {buku[kodet]['Pengarang']}, Tahun Terbit: {buku[kodet]['Tahun Terbit']}, Genre: {buku[kodet]['Genre']}")
        kon = input("Tekan Y Jika Ingin Lanjut Mengubah Data Atau N Jika Ingin Membatalkan (Y/N) :").capitalize()
        if kon == 'Y':
            kolom = input("Masukan Kolom Yang Ingin Diubah: ")
            isi_baru = input(f"Masukan {kolom} Baru: ")
            kon1 = input("Apakah Data Akan Diubah? Y/N: ").capitalize()
            if kon1 == 'Y':
                buku[kodet][kolom] = isi_baru
                print("Data Telah Diupdate")
                menu_ubah()
            else:
                print("Data Batal Diubah")
                menu_ubah()
        else:
            menu_ubah()
    else: 
        print("Buku Tidak Ditemukan")
        menu_ubah()

def menu_hapus():
    print("\n=======Hapus Data Buku Perpustakan======\n")
    print("1. Hapus Data Buku")
    print("2. Kembali ke Menu Utama")
    pilih = input("Silahkan Pilih Sub Menu Hapus Data Buku [1-2]")
    if pilih == '1':
        menu_hapus1()
    elif pilih == '2':
        menu_utama()
    else:
        menu_hapus()

def menu_hapus1():
    kode=input("Masukan Kode Buku Yang Akan Dihapus: ")
    if kode in buku.keys():
        print (buku[kode])
        kon = input("Tekan Y jika ingin lanjut menghapus data atau N jika ingin membatalkan penghapusan (Y/N) :").capitalize()
        if kon == 'Y':
            del buku[kode]
            print ("Judul Buku Telah Dihapus") 
            menu_hapus()
        else:
            menu_hapus()
    
def keluar():
    print("Anda Telah Keluar Dari Program")
    exit()

def menu_utama():
    status = True
    while status:
        print("=======Data Perpustakaan======\n")
        print("1. Tampil Data Buku")
        print("2. Tambah Data Buku")
        print("3. Ubah Data Buku")
        print("4. Hapus Data Buku")
        print("5. Keluar Program")

        for i in range (4):
            kode = input('Silahkan Pilih Sub Menu Ubah Data Buku [1-5]: ')
            if kode == '1':
                menu_tampil()
            elif kode == '2':
                menu_tambah()
            elif kode == '3':
                menu_ubah()
            elif kode == '4':
                menu_hapus()
            elif kode == '5':
                keluar()
            else:
                print("Kode yang Anda Masukan Salah")
                menu_utama()

menu_utama()

