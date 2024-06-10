class Mahasiswa:
    def __init__(self, nim, nama, angkatan, prodi):
        self.nim = nim
        self.nama = nama
        self.angkatan = angkatan
        self.prodi = prodi

    def kartu_mahasiswa(self):
        print(f"Data Mahasiswa\nNIM: {self.nim}\nNama: {self.nama}\nAngkatan: {self.angkatan}\nProdi: {self.prodi}")

    def selamat(self):
        print(f"Selamat Datang {self.nama} di Kampus UMS")

# Objek-objek Mahasiswa
mahasiswa1 = Mahasiswa("A710230006", "Nadhifa", 2023, "Pendidikan Teknik Informatika")
mahasiswa2 = Mahasiswa("A710230007", "Synta Nur", 2023, "Pendidikan Teknik Informatika")
mahasiswa3 = Mahasiswa("A710230009", "Maya Mega", 2023, "Pendidikan Teknik Informatika")

# Memanggil method kartu_mahasiswa dan selamat
mahasiswa1.kartu_mahasiswa()
mahasiswa1.selamat()
print("\n")
mahasiswa2.kartu_mahasiswa()
mahasiswa2.selamat()
print("\n")
mahasiswa3.kartu_mahasiswa()
mahasiswa3.selamat()
print("\n")
