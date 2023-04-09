#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import mysql.connector

dataBase= mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    password = ''
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE db_sales_V3922009")


# In[ ]:


import mysql.connector

dataBase= mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    password = '',
    database = "db_sales_V3922009"
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE stok_barang (
                    Id_Barang VARCHAR(20) NOT NULL PRIMARY KEY,
                    Nama_Barang VARCHAR(100),
                    Harga_Barang INT,
                    Stok_Awal INT,
                    Barang_Masuk INT,
                    Barang_Keluar INT,
                    Stok_Akhir INT
                    )"""
cursorObject.execute(studentRecord)

dataBase.close()


# In[ ]:


import mysql.connector

dataBase= mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    password = '',
    database = "db_sales_V3922009"
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO stok_barang (Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir)VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = [ ('SB001', 'Pensil 2B Faber Castell', 4000, 50, 20, 10, 60),
        ('SB002', 'Pensil Warna Joyko', 2000, 30, 15, 5, 40),
        ('SB003', 'Buku Tulis Sidu', 5000, 100, 50, 20, 130),
        ('SB004', 'Buku Gambar Kiky', 8000, 70, 25, 10, 85),
        ('SB005', 'Spidol Snowman', 3000, 40, 10, 5, 45),
        ('SB006', 'Sticky Note Kenko', 6000, 80, 30, 15, 95),
        ('SB007', 'Penghapus Joyko', 2000, 60, 20, 10, 70),
        ('SB008', 'Gunting', 7000, 50, 15, 5, 60),
        ('SB009', 'Pensil Mekanik BIG', 5000, 20, 10, 5, 25),
        ('SB010', 'Rautan Pensil Faber Castell', 5000, 30, 10, 5, 35)
      ]

cursorObject.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[ ]:


import mysql.connector

dataBase= mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    password = '',
    database = "db_sales_V3922009"
)
# membuat objek kursor untuk berinteraksi dengan database
mycursor = dataBase.cursor()

# fungsi untuk memasukkan data ke dalam tabel stok_barang
def insert_data():
    Id_Barang = input("Masukkan ID Barang: ")
    Nama_Barang = input("Masukkan Nama Barang: ")
    Harga_Barang = input("Masukkan Harga Barang: ")
    Stok_Awal = input("Masukkan Stok Awal Barang: ")
    Barang_Masuk = input("Masukkan Jumlah Barang Masuk: ")
    Barang_Keluar = input("Masukkan Jumlah Barang Keluar: ")
    Stok_Akhir = int(Stok_Awal) + int(Barang_Masuk) - int(Barang_Keluar)

    sql = "INSERT INTO stok_barang (Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir)
    mycursor.execute(sql, val)
    dataBase.commit()
    print(mycursor.rowcount, "data berhasil dimasukkan.")

# fungsi untuk menampilkan semua data dari tabel stok_barang
def show_data():
    mycursor.execute("SELECT * FROM stok_barang")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

# fungsi untuk memperbarui data di tabel stok_barang
def update_data():
    Id_Barang = input("Masukkan ID Barang yang ingin diperbarui: ")
    Nama_Barang = input("Masukkan Nama Barang baru: ")
    Harga_Barang = input("Masukkan Harga Barang baru: ")
    Stok_Awal = input("Masukkan Stok Awal Barang baru: ")
    Barang_Masuk = input("Masukkan Jumlah Barang Masuk baru: ")
    Barang_Keluar = input("Masukkan Jumlah Barang Keluar baru: ")
    Stok_Akhir = int(Stok_Awal) + int(Barang_Masuk) - int(Barang_Keluar)

    sql = "UPDATE stok_barang SET Nama_Barang = %s, Harga_Barang = %s, Stok_Awal = %s, Barang_Masuk = %s, Barang_Keluar = %s, Stok_Akhir = %s WHERE Id_Barang = %s"
    val = (Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir, Id_Barang)
    mycursor.execute(sql, val)
    dataBase.commit()
    print(mycursor.rowcount, "data berhasil diperbarui.")

# fungsi untuk menghapus data dari tabel stok_barang
def delete_data():
    Id_Barang = input("Masukkan Id Barang yang akan dihapus: ")
    sql = "DELETE FROM stok_barang WHERE Id_Barang = %s"
    val = (Id_Barang,)
    mycursor.execute(sql, val)
    dataBase.commit()
    print(mycursor.rowcount, "data berhasil dihapus.")

# fungsi untuk mencari data berdasarkan Id_Barang dari tabel stok_barang
def search_data():
    Id_Barang = input("Masukkan Id Barang yang ingin dicari: ")
    sql = "SELECT * FROM stok_barang WHERE Id_Barang = %s"
    val = (Id_Barang,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    if myresult:
        for x in myresult:
            print(x)
    else:
        print("Data tidak ditemukan.")

# fungsi untuk menampilkan pilihan menu
def tampilkan_menu():
    print("--------------------------------")
    print("Pilih menu:")
    print("1. Insert data")
    print("2. Show data")
    print("3. Update data")
    print("4. Hapus data")
    print("5. Cari data")
    print("6. Keluar")   
    
    menu = input("Pilih menu >   ")
    print("\n")

    if menu == "1":
        insert_data()
    elif menu == "2":
        show_data()
    elif menu == "3":
        update_data()
    elif menu == "4":
        delete_data()
    elif menu == "5":
        search_data()
    elif menu == "6":
        exit()
    else:
        print("Salah pilih!")


if __name__ == "__main__":
    while(True):
        tampilkan_menu()


# In[ ]:




