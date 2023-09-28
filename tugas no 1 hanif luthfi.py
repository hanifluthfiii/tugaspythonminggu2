import math

def hitung_volume_tabung(jari_jari, tinggi):
    volume = math.pi * jari_jari**2 * tinggi
    return volume

def hitung_luas_permukaan_tabung(jari_jari, tinggi):
    luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
    return luas_permukaan

def main():
    pi = 3.14

    jari_jari = float(input("jari-jari tabung: "))
    tinggi = float(input("tinggi tabung: "))

    volume = hitung_volume_tabung(jari_jari, tinggi)
    luas_permukaan = hitung_luas_permukaan_tabung(jari_jari, tinggi)

    print("Volume tabung dengan jari-jari", jari_jari, "dan tinggi", tinggi, ": ", volume)
    print("Luas permukaan tabung dengan jari-jari", jari_jari, "dan tinggi", tinggi, ": ", luas_permukaan)
