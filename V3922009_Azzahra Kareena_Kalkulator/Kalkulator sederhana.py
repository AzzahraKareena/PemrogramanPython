#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#mengimport modul tkinter
from tkinter import *

window = Tk() # untuk membuat sebuah window atau jendela GUI utama
window.title("Kalkulator GUI Dengan Python") # memberikan judul pada window
window.geometry('350x300') # digunakan untuk menentukan ukuran window (lebar x tinggi)

#objek Label dan Entry digunakan untuk membuat label dan kotak input pada jendela GUI
lbl = Label(window, text="Masukan Nilai Pertama : ",anchor="e",width=20)
lbl.grid(column=0, row=0)
#Pada baris terakhir dalam setiap blok, grid() digunakan untuk menentukan posisi label dan kotak input tersebut pada jendela GUI

nilai1 = Entry(window,width=10)
nilai1.grid(column=1,row=0)


lbl2 = Label(window, text="Masukan Nilai Kedua : ",anchor="e",width=20)
lbl2.grid(column=0, row=1)

nilai2 = Entry(window,width=10)
nilai2.grid(column=1,row=1)

lbl3 = Label(window, text="Hasil : ",anchor="e",width=20)
lbl3.grid(column=0, row=2)

hasil = Label(window, text="0",anchor="w",width=10)
hasil.grid(column=1, row=2)

#fungsi-fungsi matematika seperti penambahan, pengurangan, perkalian, pembagian, perpangkatan, modulus, dan pengakaran ditentukan pada baris-baris selanjutnya.
def tambah():
    hasil.configure(text=(float(nilai1.get())+float(nilai2.get())))

def kurang():
    hasil.configure(text=(float(nilai1.get())-float(nilai2.get())))

def kali():
    hasil.configure(text=(float(nilai1.get())*float(nilai2.get())))

def bagi():
    if nilai2.get() == '0':
        hasil.configure(text="Tidak Bisa Dibagi dengan 0")
    else:
        hasil.configure(text=(float(nilai1.get())/float(nilai2.get())))

def pangkat():
    hasil.configure(text=(float(nilai1.get())**float(nilai2.get())))
    
def pangkat2():
    hasil.configure(text=(float(nilai2.get())**float(nilai1.get())))

def modulus():
    hasil.configure(text=(float(nilai1.get())%float(nilai2.get())))

def akar():
    hasil.configure(text=(float(nilai1.get())**(1/float(nilai2.get()))))
    
def akar2():
    hasil.configure(text=(float(nilai2.get())**(1/float(nilai1.get()))))

#Fungsi-fungsi tersebut digunakan untuk menghitung hasil dari operasi matematika yang akan dilakukan oleh kalkulator
    
#Button digunakan untuk membuat tombol pada jendela GUI. Setiap tombol diatur dengan fungsi matematika yang sesuai
btnTambah = Button(window, text="Tambah", command=tambah)
btnTambah.grid(column=0, row=3)

btnKurang = Button(window, text="Kurang", command=kurang)
btnKurang.grid(column=1, row=3)

btnKali = Button(window, text="Kali", command=kali)
btnKali.grid(column=2, row=3)

btnBagi = Button(window, text="Bagi", command=bagi)
btnBagi.grid(column=3, row=3)

btnPangkat = Button(window, text="^x", command=pangkat)
btnPangkat.grid(column=0, row=4)

btnPangkat2 = Button(window, text="^y", command=pangkat2)
btnPangkat2.grid(column=1, row=4)

btnModulus = Button(window, text="%", command=modulus)
btnModulus.grid(column=2, row=4)

btnAkar = Button(window, text="akar x", command=akar)
btnAkar.grid(column=3, row=4)

btnAkar2 = Button(window, text="akar y", command=akar2)
btnAkar2.grid(column=0, row=5)

window.mainloop()


# In[ ]:




