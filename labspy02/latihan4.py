import random

n = int(input("Masukkan nilai n: "))

count = 0  # Inisialisasi jumlah bilangan acak yang sudah dihasilkan

print(f"{n} bilangan acak yang lebih kecil dari 0.5:")
while count < n:
    random_num = random.random()  # Menghasilkan bilangan acak antara 0 dan 1
    if random_num < 0.5:
        print(random_num)
        count += 1
