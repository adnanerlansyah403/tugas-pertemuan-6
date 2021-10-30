kelipatan7 = [7,14,21,28,35,42,49,56,63,70]

r = float(input("Masukkan panjang jari-jari Lingkaran : "))

for nilai in kelipatan7 :
    if r == nilai :
        phi1 = 22/7
        luaslingkaran = phi1 * r * r
        kelilinglingkaran = 2 * phi1 * r
        print("Luas Lingkaran adalah : ", int(luaslingkaran))
        print("Keliling Lingkaran adalah : ", int(kelilinglingkaran))   
        break

if r != nilai :
        phi2 = 3.14
        luaslingkaran = phi2 * r * r
        kelilinglingkaran = 2 * phi2 * r
        print("Luas Lingkaran adalah : ", float(luaslingkaran))
        print("Keliling Lingkaran adalah : ", float(kelilinglingkaran))

# penjelasan variabel r
# r merupakan representasi dari data jari-jari pada lingkaran, jadi r merupakan jari-jari yang ada pada lingkaran.
# penjelasan pengkondisian
# syarat untuk mencari luaslingkaran dan keliling lingkaran adalah
# apabila nilai/angka bersifat genap, maka akan di masukkan ke rumus phi2/ phi=22/7, dan jika nilai/angka bernilai negatif

