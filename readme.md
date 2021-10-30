# Penjelasan Program Menghitung luas dan keliling dari lingkaran

## Screen Shoot Hasil Eksekusi Program
![Gambar Output Program](ssprogram.png) <br>

### <h2> Syntax Program Python soal menghitung luas dan keliling pada lingkaran
```sh

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


```

#### <h2> Penjelasan dari Syntax pada Program Python di atas
Pada program tersebut di jelaskan untuk mengetahui luas dan keliling pada lingkaran harus sesuai dengan rumus nya. misal nya, jika data yang ingin di input atau data dari panjang
jari-jarinya adalah 5 maka ia akan masuk kedalam rumus phi = 3.14 dan jika nilainya yang di masukkan oleh input adalah kelipatan 7 maka akan di masukkan kedalam rumus phi = 22/7.
setelah di tentukan rumus phinya, maka akan di lanjut ke proses mencari luaslingkaran dan kelilinglingkaran. untuk rumus luaslingkaran adalah phi * r * r dan untuk kelilinglingkaran
adalah 2 * phi * r. jika sudah sesuai dengan prosedur atau menjumlahkan semuanya dengan rumus-rumus tadi,maka baru hasil dari program akan di print dan menjadi output. seperti yang
ada di dalam source code di atas.
