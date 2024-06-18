# Definisi kelas Orang
class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def perkenalkan_diri(self):
        print(f"Halo, nama saya {self.nama} dan saya berumur {self.umur} tahun.")

# Definisi kelas Mahasiswa yang mewarisi dari kelas Orang
class Mahasiswa(Orang):
    def __init__(self, nama, umur, jurusan):
        super().__init__(nama, umur)
        self._jurusan = jurusan

    @property
    def jurusan(self):
        return self._jurusan

    @jurusan.setter
    def jurusan(self, value):
        self._jurusan = value

# Membuat objek dari kelas Mahasiswa
mahasiswa1 = Mahasiswa("Synta", 19, "Pendidikan Teknik Informatika")

# Mengakses properti jurusan sebelum diubah
print(f"Jurusan sebelum: {mahasiswa1.jurusan}")

# Mengubah nilai properti jurusan
mahasiswa1.jurusan = "Kedokteran"

# Mengakses properti jurusan setelah diubah
print(f"Jurusan setelah: {mahasiswa1.jurusan}")
