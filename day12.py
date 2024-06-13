while True:
    try:
        # Meminta input dari user
        bilangan = int(input("Masukkan bilangan bulat: "))
        
        # Menghitung kuadrat dari bilangan yang dimasukkan
        kuadrat = bilangan ** 2
        
        # Mencetak hasil kuadrat
        print("Hasil kuadrat dari", bilangan, "adalah", kuadrat)
        
        # Keluar dari loop jika input valid dan hasil dicetak
        break
    
    except ValueError:
        # Menangani kesalahan jika input bukan bilangan bulat
        print("Input yang dimasukkan tidak valid! Masukkan bilangan bulat.")
