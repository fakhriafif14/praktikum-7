# praktikum-7
Buat program sederhana dengan input tiga buah bilangan, dari ketiga bilangan
tersebut tampilkan bilangan terbesarnya. Gunakan statement if.
<P># Meminta input dari pengguna
<br>a = float(input("Masukkan bilangan pertama: "))
<br>b = float(input("Masukkan bilangan kedua: "))
<br>c = float(input("Masukkan bilangan ketiga: "))

<P># Menggunakan statement if untuk menentukan bilangan terbesar
<br>if a > b and a > c:
   <br>bilangan_terbesar = a
<br>elif b > a and b > c:
 <br>   bilangan_terbesar = b
<br>else:
  <br>  bilangan_terbesar = c

<P># Menampilkan bilangan terbesar
<br>print("Bilangan terbesar adalah:", bilangan_terbesar)
    
# Hasil perogram
    
![gambar](ss1.png)
    
# Menampilkan flowchart
    
![gambar](flowchart.png)


# latihan 1
Buat program sederhada dengan input 2 buah bilangan, kemudian tentukan bilangan terbesar dari kedua bilangan tersebut menggunakan statement if.
<P> # Meminta input dari pengguna
<br>bilangan1 = float(input("Masukkan bilangan pertama: "))
<br>bilangan2 = float(input("Masukkan bilangan kedua: "))

<P># Menentukan bilangan terbesar
<br>if bilangan1 > bilangan2:
  <br>  terbesar = bilangan1
<br>else:
   <br> terbesar = bilangan2

<p># Menampilkan bilangan terbesar
<br>print("Bilangan terbesar adalah:", terbesar)
    
# Hasil perogram

![gambar](ss10.png)

# latihan 2
Buat program untuk mengurutkan data berdasarkan input sejumlah
data (minimal 3 variable input atau lebih), kemudian tampilkan
hasilnya secara berurutan mulai dari data terkecil.
<P># Input data dari pengguna
<br>data = []
<br>n = int(input("Masukkan jumlah data yang ingin diurutkan: "))
<br>for i in range(n):
  <br>  nilai = float(input(f"Masukkan data ke-{i + 1}: "))
  <br>  data.append(nilai)

<P># Algoritma pengurutan gelembung
<br>for i in range(n):
  <br>  for j in range(0, n - i - 1):
    <br>    if data[j] > data[j + 1]:
        <br>    data[j], data[j + 1] = data[j + 1], data[j]

<P># Menampilkan hasil pengurutan
<br>print("Data yang sudah diurutkan:")
<br>for nilai in data:
   <br> print(nilai)

   [gambar](ss3.png)


