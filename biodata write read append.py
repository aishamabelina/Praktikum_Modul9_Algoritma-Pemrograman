def write():
    nama_file = input("Masukkan nama file: ")
    nama_kamu = input("Masukkan namamu: ")
    nim_kamu = input("Masukkan NIM kamu: ")
    angkatan = input("Masukkan tahun angkatanmu: ")
    
    with open(nama_file, "w") as file:
        file.write(f"Nama: {nama_kamu}\n")
        file.write(f"NIM: {nim_kamu}\n")
        file.write(f"Tahun Angkatan: {angkatan}\n")
    print("File berhasil dibuat dan informasi berhasil ditulis.")

def read():
    nama_file = input("Masukkan nama file yang ingin dibaca: ")
    with open(nama_file, "r") as file:
        isi = file.read()
    print("Isi file:")
    print(isi)

def append():
    nama_file = input("Masukkan nama file: ")
    nama_sahabat = input("Masukkan Nama Sahabatmu: ")
    catatan_tambahan = input("Masukkan Catatan Tambahan Kamu: ")
    with open(nama_file, "a") as file:
        file.write("\nNama Sahabat: " + nama_sahabat)
        file.write("\nCatatan: " + catatan_tambahan + "\n")
    
    print("Data berhasil ditambahkan.")


def menu():
    while True:
        print("\n===== Program File Handling =====")
        print("1. Membuat dan Menulis File")
        print("2. Membaca File")
        print("3. Menambahkan Teks Pada File")
        print("4. Keluar Dari Program")
        pilihan = input("Masukkan pilihan berupa angka (1/2/3/4): ")

        if pilihan == "1":
            write()
        elif pilihan == "2":
            read()
        elif pilihan == "3":
            append()
        elif pilihan == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

menu()

