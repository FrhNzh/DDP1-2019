f = open("daftar-kucing.txt", 'r')					# membuka file
semua_kucing = set(f.read().lower().splitlines())	# membuat set nama semua kucing
n_hadir = int(input('Jumlah kucing yang hadir: '))

kucing_hadir = set()
print('\nKucing-kucing yang hadir:')
for i in range(n_hadir):							# membuat set kucing yang hadir
	nama_hadir = input().lower()
	kucing_hadir.add(nama_hadir)

print('\nKucing-kucing yang tidak hadir:')
count = 0
for i in semua_kucing:
	if i not in kucing_hadir:
		print(i)
		count += 1									# menghitung kucing yang tidak hadir

if n_hadir / len(semua_kucing) < 0.5:
	print('Yuk ikut eval!')