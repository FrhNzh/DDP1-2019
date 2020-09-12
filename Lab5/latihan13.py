def hitung_kelipatan(A,x):
	"""Fungsi untuk menghitung banyaknya angka kelipatan x"""
	counter = 0
	for i in A:
		if i % x == 0:
			counter += 1
	return counter

A = input().split()
for i in range(len(A)):
	A[i] = int(A[i])
print(hitung_kelipatan(A,3) + hitung_kelipatan(A,5) - hitung_kelipatan(A,15))

