class Tiket:
    def __init__(self, jumlah):
        self.jumlah = jumlah

    def hitung_total(self):
        pass

class TiketBiasa(Tiket):
    harga_per_tiket = 50000

    def hitung_total(self):
        return self.jumlah * self.harga_per_tiket

class TiketVIP(Tiket):
    harga_per_tiket = 100000

    def hitung_total(self):
        return self.jumlah * self.harga_per_tiket

class TiketGold(Tiket):
    harga_per_tiket = 150000

    def hitung_total(self):
        return self.jumlah * self.harga_per_tiket

def main():
    jenis_tiket = input("Masukkan jenis tiket (biasa/vip/gold) : ").lower()
    jumlah_tiket = int(input("Masukkan jumlah tiket : "))

    if jenis_tiket == 'biasa':
        tiket = TiketBiasa(jumlah_tiket)
    elif jenis_tiket == 'vip':
        tiket = TiketVIP(jumlah_tiket)
    elif jenis_tiket == 'gold':
        tiket = TiketGold(jumlah_tiket)
    else:
        print("Jenis tiket tidak valid.")
        return

    total_harga = tiket.hitung_total()
    print(f"Total Harga Tiket : Rp {total_harga:,}")

if __name__ == "__main__":
    main()
