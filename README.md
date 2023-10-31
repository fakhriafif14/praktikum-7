# praktikum 7
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

# Tugas struktur kondisi

# latihan 1
Buat program sederhana dengan input 2 buah bilangan, kemudian tentukan bilangan terbesar dari kedua bilangan tersebut menggunakan statement if.
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

   # Hasil perogram

   ![gambar](ss2.png)

   # Tugas perulangan

   # latihan 1
   Buat program dengan perulangan bertingkat (nested) for yang menghasilkan output sebagai berikut
  <P> 1.pendeklarasian variable
 <br>  baris = 10
<br>kolom = baris
<P> 2.untuk perulangan baris dan kolom menggunakan for
<br>for bar in range(baris):
   <br> for col in range(kolom):
     <br>   tab = bar+col
   <P> 3.agar terlihat rapih menggunakan format string rata kekanan sebanyak 5 karakter
       <br> agar tidak membuat garis baru menggunakan end=' ' (baris)
      <br>  print("{0:>5}".format(tab), end='')
   <br> print()

   # Hasil perogram

   ![gambar](ss3.png)

   # latihan 2
   Tampilkan n bilangan acak yang lebih kecil dari 0.5. nilai n diisi pada saat runtime anda bisa menggunakan kombinasi while dan for untuk menyelesaikannya
  <P> import random

<br>n = int(input("Masukkan nilai n: "))

<br>count = 0  # Inisialisasi jumlah bilangan acak yang sudah dihasilkan

<br>print(f"{n} bilangan acak yang lebih kecil dari 0.5:")
<br>while count < n:
  <br>  random_num = random.random()  # Menghasilkan bilangan acak antara 0 dan 1
   <br> if random_num < 0.5:
   <br>     print(random_num)
    <br>    count += 1

# Hasil perogram

![gambar](ss4.png)

   


