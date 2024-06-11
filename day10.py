# Definisi class Orang
class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def kenalan(self):
        print(f"Halo, namaku {self.nama}, umurku {self.umur}")

# Definisi class Mahasiswa yang merupakan turunan dari class Orang
class Mahasiswa(Orang):
    def __init__(self, nama, umur, universitas):
        super().__init__(nama, umur)
        self.universitas = universitas

    def kenalan(self):
        print(f"Halo, namaku {self.nama}, umurku {self.umur} dan aku kuliah di {self.universitas}")

# Definisi class Pekerja yang merupakan turunan dari class Orang
class Pekerja(Orang):
    def __init__(self, nama, umur, tempatKerja):
        super().__init__(nama, umur)
        self.tempatKerja = tempatKerja

    def kenalan(self):
        print(f"Halo, namaku {self.nama}, umurku {self.umur} dan aku kerja di {self.tempatKerja}")

# Membuat objek dari masing-masing kelas
orang1 = Orang("Baekhyun", 30)
mahasiswa1 = Mahasiswa("Chanyeol", 30, "Seoul University")
pekerja1 = Pekerja("D.o", 28, "Soosoo company")

# Memanggil method kenalan untuk setiap objek
orang1.kenalan()        # Output: Halo, namaku Baekhyun, umurku 30
mahasiswa1.kenalan()    # Output: Halo, namaku Chanyeol, umurku 30 dan aku kuliah di Seoul University
pekerja1.kenalan()      # Output: Halo, namaku D.o, umurku 28 dan aku kerja di Soosoo company
