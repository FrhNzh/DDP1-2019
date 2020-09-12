# membuka file bernama 'input.txt'
f = open('input.txt', 'r')

counter = 0

# looping setiap baris dalam file
for baris in f.readlines():
	if baris[:-1].isnumeric() == True:
		counter += 1

# mencetak banyaknya barisan yang hanya berisi angka
print(counter)