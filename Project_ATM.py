import os
import bcrypt
import re

os.system("cls")

# Tampilan header
print(f"{'='*40:^40}")
print(f"{'SELAMAT DATANG DI MESIN ATM YUDI':^40}")
print(f"{'='*40:^40}")

user_credentials = {}  # Database pengguna (untuk menyimpan kata sandi yang sudah di-hash)

# Fungsi untuk validasi kata sandi kuat
def is_strong_password(password):
    return all([
        len(password) >= 8,
        re.search(r'[a-z]', password),
        re.search(r'[A-Z]', password),
        re.search(r'[0-9]', password),
        re.search(r'[!@#$%^&*]', password)
    ])

while True:
    # Tampilan menu utama
    print(f"{'===> MENU UTAMA <===':^40}\n1. MASUK AKUN\n2. REGISTRASI\n3. KELUAR\n")
    log_or_reg = input("Pilihan opsi: ")

    if log_or_reg == "1":
        # Masuk akun
        print(f"{'='*40:^40}\n{'MASUK AKUN':^40}\n{'='*40:^40}\n")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username in user_credentials and bcrypt.checkpw(password.encode('utf-8'), user_credentials[username]):
            print(f"{'='*40:^40}\n{'MASUK BERHASIL':^40}\n{'='*40:^40}\n")
        else:
            print("\n" + "-"*40 + "\nAnda belum memiliki akun! Silahkan REGISTRASI terlebih dahulu\n" + "-"*40)

    elif log_or_reg == "2":
        # Registrasi
        print(f"{'='*40:^40}\n{'REGISTRASI':^40}\n{'='*40:^40}\n")

        while True:
            new_username = input("Masukkan username: ")
            new_password = input("Masukkan password: ")

            if not new_username or not new_password:
                print("\n*Maaf Username atau Password tidak boleh kosong!\n")
            elif new_username in user_credentials:
                print("\nMaaf Username sudah digunakan! Mohon gunakan Username lain\n")
            elif not is_strong_password(new_password):
                print("\n*Password harus memiliki setidaknya 8 karakter, termasuk huruf besar, huruf kecil, angka, dan karakter khusus\n")
            else:
                isBenar = input("Masukkan password sekali lagi: ")

                if isBenar == new_password:
                    salt = bcrypt.gensalt()
                    hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), salt)
                    user_credentials[new_username] = hashed_password

                    if new_username in user_credentials and bcrypt.checkpw(new_password.encode('utf-8'), user_credentials[new_username]):
                        print("-"*40)
                        print("Anda berhasil untuk REGISTRASI")
                        print("-"*40)
                        break
                else:
                    print("\n*Password yang Anda masukkan tidak sama!\n")

    elif log_or_reg == "3":
        # Keluar dari program
        print(f"{'='*40:^40}\n{'PROGRAM SELESAI':^40}\n{'='*40:^40}\n")
        break
    else:
        # Pilihan opsi tidak valid
        print("\n" + "-"*40 + "\nInput yang anda masukkan tidak valid! Silahkan masukkan 1, 2 atau 3!\n" + "-"*40)
