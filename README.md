# praktikum-7
Buat program sederhana dengan input tiga buah bilangan, dari ketiga bilangan
tersebut tampilkan bilangan terbesarnya. Gunakan statement if.
<P># Meminta input dari pengguna
<br>a = float(input("Masukkan bilangan pertama: "))
b = float(input("Masukkan bilangan kedua: "))
c = float(input("Masukkan bilangan ketiga: "))

<P># Menggunakan statement if untuk menentukan bilangan terbesar
<br>if a > b and a > c:
    bilangan_terbesar = a
elif b > a and b > c:
    bilangan_terbesar = b
else:
    bilangan_terbesar = c

<P># Menampilkan bilangan terbesar
</P>print("Bilangan terbesar adalah:", bilangan_terbesar)
