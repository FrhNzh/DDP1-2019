
counter = int('0')
print(counter)

# meminta user memasukan operasi
operasi = input().lower()

# me-loop operasi
while True:
	if operasi == 'tambah':
		counter += 1
		print(counter)
	elif operasi == 'kurang':
		counter -= 1
		if counter < 0:
			print('Angka negatif\nselesai')
			break
		print(counter)
	elif operasi == 'selesai':
		print('SELESAI')
		break
	operasi = input().lower()