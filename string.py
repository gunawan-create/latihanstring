import re

def validasi_form(nama, nomor_telepon, email):
    errors = []

    if not nama.isalpha():
        errors.append("Nama lengkap harus hanya berisi huruf.")

    if not nomor_telepon.isdigit():
        errors.append("Nomor telepon harus hanya berisi angka.")

    if "@" not in email or "." not in email:
        errors.append("Email harus mengandung karakter '@' dan '.'.")

    if errors:
        for error in errors:
            print(error)
    else:
        print("Data pendaftaran valid.")

nama = input("Masukkan nama lengkap: ")
nomor_telepon = input("Masukkan nomor telepon: ")
email = input("Masukkan email: ")

validasi_form(nama, nomor_telepon, email)