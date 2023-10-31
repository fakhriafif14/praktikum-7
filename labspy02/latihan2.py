# Input data dari pengguna
data = []

n = int(input("Masukkan jumlah data yang ingin diurutkan: "))

for i in range(n):
    nilai = float(input(f"Masukkan data ke-{i + 1}: "))
    data.append(nilai)

# Algoritma pengurutan gelembung
for i in range(n):
    for j in range(0, n - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

# Menampilkan hasil pengurutan
print("Data yang sudah diurutkan:")
for nilai in data:
    print(nilai)
