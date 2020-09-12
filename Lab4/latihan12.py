# membuka file dengan nama 'input.txt'
f = open('input.txt', 'r')

list = []
counter = 0

# looping untuk mengecek baris yang hanya berisi angka
for baris in f.read().split('\n'):
	if baris.isnumeric() == True:
		x = int(baris[::-1])
		list.append(x)

# mencari nilai maksimum pada list
maksimum = max(list)
list.remove(maksimum)

# mencetak nilai pada list
for i in list:
	print(i)