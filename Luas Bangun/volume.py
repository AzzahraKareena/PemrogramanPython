import math

def kubus(sisi):
    return sisi**3

def balok(panjang, lebar, tinggi):
    return panjang*lebar*tinggi

def tabung(jari_jari, tinggi):
    return math.pi*jari_jari**2*tinggi

def kerucut(jari_jari, tinggi):
    return 1/3*math.pi*jari_jari**2*tinggi

def limas(alas, tinggi):
    return 1/3*alas*tinggi

def prisma(alas, tinggi_prisma):
    return alas*tinggi_prisma