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

cursorObject.execute("CREATE DATABASE D3_TI_2023")


# In[ ]:


import mysql.connector

dataBase= mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    password = '',
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE Mata_Kuliah (
                    Kode_MK VARCHAR(10) PRIMARY KEY,
                    Nama_MK VARCHAR(50),
                    Waktu DATE,
                    Ruangan VARCHAR(10)
                    );
                    CREATE TABLE Mahasiswa (
                    NIM VARCHAR(10) PRIMARY KEY,
                    Nama VARCHAR(30),
                    Alamat VARCHAR(255),
                    Mata_Kuliah_Ikut VARCHAR(10),
                    FOREIGN KEY (Mata_Kuliah_Ikut) REFERENCES Mata_Kuliah(Kode_MK)
                    );
                    CREATE TABLE DOSEN (
                    NIP VARCHAR(20) PRIMARY KEY,
                    Nama_Dosen VARCHAR(50),
                    Mata_Kuliah_Ajar VARCHAR(10),
                    FOREIGN KEY (Mata_Kuliah_Ajar) REFERENCES Mata_Kuliah(Kode_MK)
                    );"""
cursorObject.execute(studentRecord)

dataBase.close()


# In[ ]:


import mysql.connector

dataBase= mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    password = '',
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO Mata_Kuliah (Kode_MK, Nama_MK, Waktu, Ruangan)VALUES (%s, %s, %s, %s)"
val = [ ('MK001', 'Pemrograman Web', '2023-04-10', 'A101'),
        ('MK002', 'Basis Data', '2023-04-12', 'B201'),
        ('MK003', 'Jaringan Komputer', '2023-04-14', 'C301'),
        ('MK004', 'Sistem Operasi', '2023-04-16', 'D401'),
        ('MK005', 'Algoritma dan Struktur Data', '2023-04-18', 'E501'),
        ('MK006', 'Pemrograman Mobile', '2023-04-20', 'F601')
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
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO Mahasiswa (NIM, Nama, Alamat, Mata_Kuliah_Ikut)VALUES (%s, %s, %s, %s)"
val = [ ('V392101', 'Cantika', 'Jl. Sudirman, Caruban', 'MK001'),
        ('V392102', 'Anita', 'Jl. Gatot Subroto, Madiun', 'MK002'),
        ('V392103', 'Cintya', 'Jl. Thamrin, Madiun', 'MK003'),
        ('V392104', 'Dani', 'Jl. Diponegoro, Madiun', 'MK004'),
        ('V392105', 'Putri', 'Jl. Merdeka, Jiwan', 'MK005'),
        ('V392106', 'Fanita', 'Jl. Gajah Mada, Caruban', 'MK006')
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
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO Dosen (NIP, Nama_Dosen, Mata_Kuliah_Ajar)VALUES (%s, %s, %s)"
val = [ ('1987538328', 'Masbahah', 'MK001'),
        ('1932837523', 'Masbahah', 'MK002'),
        ('1952428154', 'Yusuf Fadlila', 'MK003'),
        ('1973527347', 'Nur Azzizul', 'MK004'),
        ('1963725382', 'Masbahah', 'MK005'),
        ('1926518592', 'Darmawan Lahru', 'MK006')
      ]

cursorObject.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[9]:


import mysql.connector

dataBase= mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    password = '',
    database = "D3_TI_2023"
)

cursorObject = dataBase.cursor()

# Query untuk menampilkan data mata kuliah yang diikuti oleh mahasiswa beserta dosen yang mengajar
query = "SELECT Mahasiswa.NIM, Mahasiswa.Nama AS Nama_Mahasiswa, Mata_Kuliah.Nama_MK AS Mata_Kuliah, Dosen.Nama_Dosen          FROM Mahasiswa          INNER JOIN Mata_Kuliah ON Mahasiswa.Mata_Kuliah_Ikut = Mata_Kuliah.Kode_MK          INNER JOIN Dosen ON Dosen.Mata_Kuliah_Ajar = Dosen.Mata_Kuliah_Ajar"

# Mengeksekusi query
cursorObject.execute(query)

# Menampilkan data
for data in cursorObject.fetchall():
    print("NIM        : ", data[0])
    print("Mahasiswa  : ", data[1])
    print("Mata Kuliah: ", data[2])
    print("Dosen      : ", data[3])
    print()
    
# Menutup koneksi ke database
dataBase.close()


# In[ ]:




