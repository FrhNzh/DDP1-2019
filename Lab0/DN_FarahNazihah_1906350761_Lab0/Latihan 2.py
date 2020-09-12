# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Meminta user memasukan sisi trapesium
print("Masukan panjang a") 
panjang_a = float(input()) #sisi atas trapesium

print("Masukan panjang b") 
panjang_b = float(input()) #alas trapesium

print("Masukan panjang h") 
panjang_h = float(input()) #tinggi trapesium


# Menghitung luas trapesium
luas_trapesium = (panjang_a + panjang_b) / 2 * panjang_h
print("Luas trapesium = ", luas_trapesium)