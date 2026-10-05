import os
import sys
import time

data_akun = {
    "admin": {"password": "123", "role": "admin"},
    "user": {"password": "123", "role": "user"},
}

daftar_proyek = {
    "1": {"nama": "Gemi", "jenis": "Undangan & Stiker", "deadline": "25 Mei"},
    "2": {"nama": "Lida", "jenis": "Logo", "deadline": "09 Mei"},
}

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def tampilkan_data():
    print("--- DAFTAR PROYEK ---")
    if len(daftar_proyek) == 0:
        print("Belum ada data proyek.")
    else:
        for id_proyek, detail in daftar_proyek.items():
            print("ID Proyek    :", id_proyek)
            print("Nama Klien   :", detail["nama"])
            print("Jenis Desain :", detail["jenis"])
            print("Deadline     :", detail["deadline"])
            print("-----------------------------")


def tambah_data():
    print("--- TAMBAH PROYEK BARU ---")
    id_baru = str(len(daftar_proyek) + 1)

    nama = input("Masukkan nama klien: ")
    jenis = input("Masukkan jenis desain: ")
    deadline = input("Masukkan deadline: ")

    if nama != "" and jenis != "" and deadline != "":
        daftar_proyek[id_baru] = {
            "nama": nama,
            "jenis": jenis,
            "deadline": deadline,
        }
        print("Data berhasil ditambahkan!")
    else:
        print("Error: Semua data wajib diisi!")


def ubah_data():
    tampilkan_data()
    if len(daftar_proyek) == 0:
        return

    print("--- UBAH DATA PROYEK ---")
    id_pilih = input("Masukkan ID proyek yang mau diubah: ")

    # Validasi keberadaan ID
    if id_pilih in daftar_proyek:
        print("(Tekan Enter jika tidak ingin mengubah data)")
        nama_baru = input(f"Nama klien baru [{daftar_proyek[id_pilih]['nama']}]: ")
        jenis_baru = input(
            f"Jenis desain baru [{daftar_proyek[id_pilih]['jenis']}]: "
        )
        deadline_baru = input(
            f"Deadline baru [{daftar_proyek[id_pilih]['deadline']}]: "
        )

        if nama_baru != "":
            daftar_proyek[id_pilih]["nama"] = nama_baru
        if jenis_baru != "":
            daftar_proyek[id_pilih]["jenis"] = jenis_baru
        if deadline_baru != "":
            daftar_proyek[id_pilih]["deadline"] = deadline_baru

        print("Data berhasil diperbarui!")
    else:
        print("ID proyek tidak ditemukan!")

def hapus_data():
    tampilkan_data()
    if len(daftar_proyek) == 0:
        return

    print("--- HAPUS DATA PROYEK ---")
    id_pilih = input("Masukkan ID proyek yang mau dihapus: ")

    if id_pilih in daftar_proyek:
        del daftar_proyek[id_pilih]
        print("Data berhasil dihapus!")
    else:
        print("ID proyek tidak ditemukan!")

def menu_admin():
    while True:
        bersihkan_layar()
        print("MENU PROYEK DESAIN (ADMIN)")
        print("1. Tampilkan Data Proyek")
        print("2. Tambah Data Proyek")
        print("3. Ubah Data Proyek")
        print("4. Hapus Data Proyek")
        print("5. Logout")

        try:
            pilihan = int(input("Pilih menu (1-5): "))
            print()

            if pilihan == 1:
                tampilkan_data()
                input("\nTekan Enter untuk kembali...")
            elif pilihan == 2:
                tambah_data()
                input("\nTekan Enter untuk kembali...")
            elif pilihan == 3:
                ubah_data()
                input("\nTekan Enter untuk kembali...")
            elif pilihan == 4:
                hapus_data()
                input("\nTekan Enter untuk kembali...")
            elif pilihan == 5:
                print("Logout berhasil!")
                time.sleep(1)
                break
            else:
                print("Pilihan menu tidak valid, silakan masukkan angka 1-5.")
                time.sleep(1)
        except ValueError:
            print("Error: Masukkan input berupa angka!")
            time.sleep(1)

def menu_user():
    while True:
        bersihkan_layar()
        print("MENU PROYEK DESAIN (USER)")
        print("1. Tampilkan Data Proyek")
        print("2. Logout")

        try:
            pilihan = int(input("Pilih menu (1-2): "))
            print()

            if pilihan == 1:
                tampilkan_data()
                input("Tekan Enter untuk kembali...")
            elif pilihan == 2:
                print("Logout berhasil!")
                time.sleep(1)
                break
            else:
                print("Pilihan menu tidak valid, silakan masukkan angka 1-2.")
                time.sleep(1)
        except ValueError:
            print("Error: Masukkan input berupa angka!")
            time.sleep(1)


def main():
    while True:
        bersihkan_layar()
        print("=== SISTEM LOGIN PROYEK DESAIN ===")
        username = input("Username: ")
        password = input("Password: ")

        if username in data_akun and data_akun[username]["password"] == password:
            role = data_akun[username]["role"]
            print("Login berhasil sebagai {role.upper()}!")
            time.sleep(1)

            if role == "admin":
                menu_admin()
            elif role == "user":
                menu_user()
        else:
            print("Username atau password salah!")
            time.sleep(1)

        ulang = input("Ingin login lagi? (y/n): ")
        if ulang.lower() != "y":
            print("Program selesai. Terima kasih!")
            sys.exit()

main()
