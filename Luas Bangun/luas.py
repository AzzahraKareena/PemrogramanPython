import math

def persegi(sisi):
    return sisi**2

def persegi_panjang(panjang, lebar):
    return panjang*lebar

def segitiga(alas, tinggi):
    return 0.5*alas*tinggi

def lingkaran(jari_jari):
    return math.pi*jari_jari**2

def jajar_genjang(alas, tinggi):
    return alas*tinggi

def trapesium(sisi_a, sisi_b, tinggi):
    return 0.5*(sisi_a+sisi_b)*tinggi