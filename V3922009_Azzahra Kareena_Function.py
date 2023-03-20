#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Fungsi untuk menghitung FPB
def hitung_fpb(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Fungsi untuk menghitung KPK
def hitung_kpk(a, b):
    return (a * b) // hitung_fpb(a, b)

# Menu utama
while True:
    print("----------PILIH PERHITUNGAN------------")
    print("1. Hitung FPB")
    print("2. Hitung KPK")
    print("3. Keluar")

    pilihan = int(input("Masukkan pilihan: "))

    if pilihan == 1:
        bilangan1 = int(input("Masukkan bilangan pertama: "))
        bilangan2 = int(input("Masukkan bilangan kedua: "))

        fpb = hitung_fpb(bilangan1, bilangan2)
        print("FPB dari", bilangan1, "dan", bilangan2, "adalah", fpb)

    elif pilihan == 2:
        bilangan1 = int(input("Masukkan bilangan pertama: "))
        bilangan2 = int(input("Masukkan bilangan kedua: "))

        kpk = hitung_kpk(bilangan1, bilangan2)
        print("KPK dari", bilangan1, "dan", bilangan2, "adalah", kpk)

    elif pilihan == 3:
        break

    else:
        print("ALERT!!")


# In[ ]:




