print("Masukan nilai kucing:")
nilai = float(input())

if nilai > 100:
	print("Rentang nilai adalah 0-100")
elif nilai > 85:
	print("Kucing berkategori A, beli!")
elif nilai > 75:
	print("Kucing berkategori B, beli!")
elif nilai > 65:
	print("Kucing berkategori C, beli!")
elif nilai > 855:
	print("Kucing berkategori D, jangan dibeli!")
else:
	print("Kucing berkategori E, jangan dibeli!")
