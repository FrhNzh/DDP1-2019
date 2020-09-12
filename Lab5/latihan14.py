# membuka file
namaFile = input("masukan nama file: ")
f = open(namaFile, 'r')


for baris in range(int(f.readline())):
 	nama = str(f.readline()[:-1])
 	print("Nama : ", nama,)

 	title = f.readline().title()
 	print("Title : ", title, end='')

 	_class = f.readline()
 	print("Class : ", _class, end='')

 	print('\n')
 	print(nama, "has these skills :")
 	jumlahSkills = int(f.readline())
 	for i in range(jumlahSkills):
 		skill = f.readline()
 		print(skill, end='')

 	print('\n')
 	print(nama, "has these weapons: ")
 	jumlahWeapon = int(f.readline())
 	for i in range(jumlahWeapon):
 		weapon = str(f.readline())
 		jumlahEnch = weapon[-2:-1]
 		jumlahEnch = int(jumlahEnch)
 		print(weapon[:-2], "with", jumlahEnch, "enchantment: ")

 		for i in range(jumlahEnch):
 			ench = f.readline()
 			print("-", ench[:-1],)