
# meminta input ordo matriks
ordo = input('ordo matriks: ')
m, n = ordo.split(' ')
baris = int(m)
kolom = int(n)


def list_matriks(baris):
	'''mengubah matriks menjadi list'''

	lst = []
	for i in range(baris):
		temp = input()
		cek = []
		for i in temp.split():
			lst.append(int(i))

	return lst


# membuat list matriks pertama
print("matriks 1:")
matriks1 = list_matriks(baris)
while len(matriks1) != kolom*baris:
	print("Tolong masukan matriks sesuai ordo")
	matriks1 = list_matriks(baris)

# membuat list matriks kedua
print("matriks 2:")
matriks2 = list_matriks(baris)
while len(matriks2) != kolom*baris:
	print("Tolong masukan matriks sesuai ordo")
	matriks2 = list_matriks(baris)

# menjumlahkan matriks
hasil = []
counter = 0
for i in range(len(matriks1)):
	jumlah = matriks1[counter] + matriks2[counter]
	counter +=1
	hasil.append(jumlah)

# mencetak matriks hasil penjumlahan
print("\nmatriks hasil:")
counter = 0
for i in range(baris):
	for i in range(kolom):
		print(hasil[counter], end=' ')
		counter +=1
	print()

'''
note :
agak diubah ada tulisannya gpp ya kak, pusing bacanya kalo gada buset
gapake template karna baru ngescroll setelah kelar ngerjain
'''