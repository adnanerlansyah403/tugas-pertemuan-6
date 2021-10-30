# Penjelasan Program Menghitung luas dan keliling dari lingkaran
## <h4 style="text-align:center;justify-content:center;"> Screen Shoot Hasil Eksekusi Program
![Gambar Output Program](ssprogram.png)
###<h4> Syntax Program Python soal menghitung luas dan keliling pada lingkaran
<br>
```sh
<br>
kelipatan7 = [7,14,21,28,35,42,49,56,63,70]
<br>
r = float(input("Masukkan panjang jari-jari Lingkaran : "))
<br>
for nilai in kelipatan7 : <br>
    if r == nilai : <br>
        phi1 = 22/7 <br>
        luaslingkaran = phi1 * nilai * nilai <br>
        kelilinglingkaran = 2 * phi1 * nilai <br>
        print("Luas Lingkaran adalah : ", int(luaslingkaran)) <br>
        print("Keliling Lingkaran adalah : ", int(kelilinglingkaran)) <br>   
        break <br>
<br>
if r != nilai : <br>
        phi2 = 3.14 <br>
        luaslingkaran = phi2 * r * r <br>
        kelilinglingkaran = 2 * phi2 * r <br>
        print("Luas Lingkaran adalah : ", float(luaslingkaran)) <br>
        print("Keliling Lingkaran adalah : ", float(kelilinglingkaran)) <br>
<br>

```
