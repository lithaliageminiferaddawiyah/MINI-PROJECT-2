import os
import time
from prettytable import PrettyTable
import pwinput

akun = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

daftar_proyek = {
    1: {"klien": "Gemi", "jenis": "Undangan & Stiker", "deadline": "25 Mei"},
    2: {"klien": "Lida", "jenis": "Logo", "deadline": "09 Mei"}
}

def bersih():
    os.system("cls" if os.name == "nt" else "clear")

def tampil_proyek():
    if daftar_proyek == {}:
        print("Data proyek masih kosong.")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["No", "Nama Klien", "Jenis Desain", "Deadline"]
        for nomor in daftar_proyek:
            tabel.add_row([nomor, daftar_proyek[nomor]["klien"], daftar_proyek[nomor]["jenis"], daftar_proyek[nomor]["deadline"]])
        print(tabel)

def tambah_proyek():
    global nomor_baru
    print("--- TAMBAH PROYEK BARU ---")
    nama = input("Masukkan nama klien: ")
    jenis = input("Masukkan jenis desain: ")
    deadline = input("Masukkan deadline: ")

    if nama == "" or jenis == "" or deadline == "":
        print("Data tidak boleh kosong!")
    else:
        daftar_proyek[nomor_baru] = {"klien": nama, "jenis": jenis, "deadline": deadline}
        nomor_baru += 1
        print("Data berhasil ditambahkan!")

def ubah_proyek():
    print("--- UBAH PROYEK ---")
    tampil_proyek()
    try:
        nomor = int(input("Masukkan nomor proyek yang diubah: "))
        if nomor in daftar_proyek:
            nama = input("Nama klien baru: ")
            jenis = input("Jenis desain baru: ")
            deadline = input("Deadline baru: ")
            if nama == "" or jenis == "" or deadline == "":
                print("Data tidak boleh kosong!")
            else:
                daftar_proyek[nomor] = {"klien": nama, "jenis": jenis, "deadline": deadline}
                print("Data berhasil diubah!")
        else:
            print("Nomor proyek tidak ada!")
    except ValueError:
        print("Input harus berupa angka!")

def hapus_proyek():
    print("--- HAPUS PROYEK ---")
    tampil_proyek()
    try:
        nomor = int(input("Masukkan nomor proyek yang dihapus: "))
        if nomor in daftar_proyek:
            del daftar_proyek[nomor]
            print("Data berhasil dihapus!")
        else:
            print("Nomor proyek tidak ada!")
    except ValueError:
        print("Input harus berupa angka!")

def cari_proyek():
    print("--- CARI PROYEK ---")
    cari = input("Masukkan nama klien: ")
    ketemu = False
    for nomor in daftar_proyek:
        if cari == daftar_proyek[nomor]["klien"]:
            print("Nama Klien   :", daftar_proyek[nomor]["klien"])
            print("Jenis Desain :", daftar_proyek[nomor]["jenis"])
            print("Deadline     :", daftar_proyek[nomor]["deadline"])
            ketemu = True
    if ketemu == False:
        print("Klien tidak ditemukan.")

def menu_admin():
    pilihan = ""
    while pilihan != "5":
        bersih()
        print("MENU ADMIN")
        print("1. Tampilkan Data Proyek")
        print("2. Tambah Data Proyek")
        print("3. Ubah Data Proyek")
        print("4. Hapus Data Proyek")
        print("5. Logout")
        pilihan = input("Pilih menu (1-5): ")
        print()

        if pilihan == "1":
            tampil_proyek()
        elif pilihan == "2":
            tambah_proyek()
        elif pilihan == "3":
            ubah_proyek()
        elif pilihan == "4":
            hapus_proyek()
        elif pilihan == "5":
            print("Logout berhasil.")
        else:
            print("Pilihan menu tidak valid, masukkan angka 1-5.")
        time.sleep(4)

def menu_user():
    pilihan = ""
    while pilihan != "3":
        bersih()
        print("MENU USER")
        print("1. Tampilkan Data Proyek")
        print("2. Cari Proyek")
        print("3. Logout")
        pilihan = input("Pilih menu (1-3): ")
        print()

        if pilihan == "1":
            tampil_proyek()
        elif pilihan == "2":
            cari_proyek()
        elif pilihan == "3":
            print("Logout berhasil.")
        else:
            print("Pilihan menu tidak valid, masukkan angka 1-3.")
        time.sleep(4)

def login():
    kesempatan = 3
    while kesempatan > 0:
        print("=== LOGIN ===")
        username = input("Username: ")
        password = pwinput.pwinput("Password: ")

        if username in akun and akun[username]["password"] == password:
            print("Login berhasil!")
            time.sleep(1)
            if akun[username]["role"] == "admin":
                menu_admin()
            else:
                menu_user()
            return
        else:
            kesempatan -= 1
            print("Username atau password salah! Sisa kesempatan:", kesempatan)
    print("Kesempatan login habis.")

pilihan = ""
while pilihan != "2":
    bersih()
    print("MENU PROYEK DESAIN")
    print("1. Login")
    print("2. Keluar")
    pilihan = input("Pilih menu (1-2): ")
    print()

    if pilihan == "1":
        login()
        time.sleep(5)
    elif pilihan == "2":
        print("Program selesai. Terima kasih!")
    else:
        print("Pilihan menu tidak valid, masukkan angka 1 atau 2.")
        time.sleep(4)