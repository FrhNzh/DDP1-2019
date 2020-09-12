import csv
from operator import itemgetter

class Budaya:
	def __init__(self, nama, tipe, prov, ref):
		self.nama = nama
		self.tipe = tipe
		self.prov = prov
		self.ref = ref

	def get_nama(self):
		return self.nama.lower()

	def get_tipe(self):
		return self.tipe.lower()

	def get_prov(self):
		return self.prov.lower()

	def get_ref(self):
		return self.ref.lower()

	def __str__(self):
		return ("{},{},{},{}".format(self.nama, self.tipe, self.prov, self.ref))


def impor(dict_budaya, nama_file):
	''' Fungsi untuk mengimpor file'''
	
	try:
		with open(nama_file, 'r') as myfile:
			file_reader = csv.reader(myfile)

			counter = 0
			for i in file_reader:
				nama, tipe, prov, ref = i
				
				if nama.lower() in dict_budaya:
					print("Budaya {0} sudah terdata. Budaya {0} berhasil diupdate.".format(nama))

				objek = Budaya(nama.title(), tipe.title(), prov.title(), ref)
				dict_budaya[objek.get_nama()] = objek
				counter += 1
		
		print("Terimpor {} baris".format(counter))
	except FileNotFoundError:
		print("File tidak ditemukan.")
	
	return dict_budaya


def ekspor(dict_budaya, nama_file):
	''' Fungsi untuk mengekspor data ke suatu file csv '''

	with open(nama_file, 'w', newline='') as csvfile:
		file_writer = csv.writer(csvfile, delimiter=',')
		for i in dict_budaya:
			file_writer.writerow([i, dict_budaya[i].tipe, dict_budaya[i].prov, dict_budaya[i].ref])
	
	print("{} budaya berhasil diekspor".format(len(dict_budaya)))


def cari_nama(dict_budaya, nama):
	''' Fungsi untuk mencari budaya dalam data '''

	if len(dict_budaya) == 0:
		print("Belum ada data warisan budaya.")
		print("Gunakan perintah \"impor\" atau \"tambah\" untuk menambahkan budaya ke dalam data.")
	elif nama == "*":
		print("Terdapat {} budaya.".format(len(dict_budaya)))
		for i in dict_budaya:
			print(dict_budaya[i])
	else:
		try:
			objek = dict_budaya[nama]
			print(objek)
		except KeyError:
			print("{} tidak ditemukan".format(nama))


def cari_tipe(dict_budaya, tipe):
	''' Fungsi untuk mencari budaya berdasarkan tipe dalam data '''

	if len(dict_budaya) == 0:
		print("Belum ada data warisan budaya.")
		print("Gunakan perintah \"impor\" atau \"tambah\" untuk menambahkan budaya ke dalam data.")
	else:
		lst = []
		for i in dict_budaya:
			if dict_budaya[i].tipe.lower() == tipe:
				lst.append(dict_budaya[i])
		
		print("Ditemukan {} budaya".format(len(lst)))
		for i in lst:
			print(i)


def cari_prov(dict_budaya, prov):
	''' Fungsi untuk mencari budaya berdasarkan provinsi dalam data '''

	if len(dict_budaya) == 0:
		print("Belum ada data warisan budaya.")
		print("Gunakan perintah \"impor\" atau \"tambah\" untuk menambahkan budaya ke dalam data.")
	else:
		lst = []
		for i in dict_budaya:
			if dict_budaya[i].prov.lower() == prov:
				lst.append(dict_budaya[i])
		
		print("Ditemukan {} budaya".format(len(lst)))
		for i in lst:
			print(i)


def tambah(dict_budaya, objek):
	''' Fungsi untuk menambah budaya ke dalam data '''
	if ";;;" not in objek:
		print("Gunakan \";;;\" untuk memisahkan setiap kata")
		print("Contoh: Tahu Gejrot;;;Makanan;;;Jawa Barat;;;https://id.wikipedia.org/wiki/Tahu_gejrot")
	else:
		try:
			nama, tipe, prov, ref = objek.split(";;;")
		except ValueError:
			print("Harus terdapat 4 data untuk setiap budaya.")
			print("Dengan format <Nama Budaya>;;;<Tipe>;;;<Provinsi>;;;<reference url>")
		if nama in dict_budaya:
			print("Budaya {} sudah ada di dalam data. Gunakan perintah \"update\" jika ingin meng-update budaya.".format(nama))
		else:
			objek = Budaya(nama, tipe, prov, ref)
			dict_budaya[objek.get_nama()] = objek	
			print("{} berhasil ditambahkan".format(nama))

		return dict_budaya


def update(dict_budaya, objek):
	''' Fungsi untuk meng-update budaya yang sudah tersedia dalam data '''

	if len(dict_budaya) == 0:
		print("Belum ada data warisan budaya.")
		print("Gunakan perintah \"impor\" atau \"tambah\" untuk menambahkan budaya ke dalam data.")
	elif ";;;" not in objek:
		print("Gunakan \";;;\" untuk memisahkan setiap kata")
		print("Contoh: Tahu Gejrot;;;Makanan;;;Jawa Barat;;;https://id.wikipedia.org/wiki/Tahu_gejrot")
	else:
		try:
			nama, tipe, prov, ref = objek.split(";;;")
		
			if nama.lower() not in dict_budaya:
				print("Budaya {} tidak ditemukan. Gunakan perintah \"tambah\" jika ingin menambahkan budaya.".format(nama))
			else:
				objek = Budaya(nama, tipe, prov, ref)
				dict_budaya[objek.nama] = objek	
				print("{} berhasil diupdate".format(nama))

		except ValueError:
			print("Harus terdapat 4 data untuk setiap budaya.")
			print("Dengan format <Nama Budaya>;;;<Tipe>;;;<Provinsi>;;;<reference url>")
	return dict_budaya


def stat(dict_budaya):
	''' Fungsi untuk menampilkan jumlah budaya di dalam data'''

	if len(dict_budaya) == 0:
		print("Belum ada data warisan budaya.")
		print("Gunakan perintah \"impor\" atau \"tambah\" untuk menambahkan budaya ke dalam data.")
	else:
		print("Terdapat {} warisan budaya".format(len(dict_budaya)))
	

def stat_tipe(dict_budaya):
	''' Fungsi untuk menghitung jumlah budaya berdasarkan tipe '''

	if len(dict_budaya) == 0:
		print("Belum ada data warisan budaya.")
		print("Gunakan perintah \"impor\" atau \"tambah\" untuk menambahkan budaya ke dalam data.")
	else:
		dict_stat = dict()
		for i in dict_budaya:
			try :
				dict_stat[dict_budaya[i].tipe] += 1
			except KeyError:
				dict_stat[dict_budaya[i].tipe] = 1
	
		lst_stat = []
		for i in dict_stat:
			lst_stat.append((i, dict_stat[i]))

		print(sorted(lst_stat, key=itemgetter(1), reverse=True))
	

def stat_prov(dict_budaya):
	''' Fungsi untuk menghitung jumlah budaya berdasarkan provinsi '''

	if len(dict_budaya) == 0:
		print("Belum ada data warisan budaya.")
		print("Gunakan perintah \"impor\" atau \"tambah\" untuk menambahkan budaya ke dalam data.")
	else:
		dict_stat = dict()
		for i in dict_budaya:
			try :
				dict_stat[dict_budaya[i].prov] += 1
			except KeyError:
				dict_stat[dict_budaya[i].prov] = 1
		
		lst_stat = []
		for i in dict_stat:
			lst_stat.append((i, dict_stat[i]))

		print(sorted(lst_stat, key=itemgetter(1), reverse=True))


def hapus(dict_budaya, nama):
	''' Fungsi untuk menghapus budaya dari data '''

	if len(dict_budaya) == 0:
		print("Belum ada data warisan budaya.")
		print("Gunakan perintah \"impor\" atau \"tambah\" untuk menambahkan budaya ke dalam data.")
	elif nama == "*":
		print("Semua data Budaya berhasil dihapus.")
		dict_budaya = dict()
	else:
		try:
			del dict_budaya[nama]
			print("{} berhasil dihapus".format(nama))
		except KeyError:
			print("Budaya {0} tidak ditemukan. {0} gagal dihapus.".format(nama))

	return dict_budaya



def bantuan():
	''' Fungsi untuk menampilkan semua perintah '''

	print("Perintah yang tersedia:")
	print("""\
- impor, untuk mengimpor data dari file csv.
- ekspor, untuk mengekspor data menjadi file csv dengan nama tertentu.
- carinama, untuk mencari nama budaya.
- caritipe, untuk mencari tipe budaya.
- cariprov, untuk mencari provinsi budaya.
- tambah, untuk menambahkan budaya.
- update, untuk meng-update budaya.
- stat, untuk menampilkan jumlah budaya yang tersedia.
- stattipe, untuk menampilkan tipe budaya beserta jumlahnya pada data.
- statprov, untuk menampilkan provinsi budaya beserta jumlahnya pada data.
- hapus, untuk menghapus budaya dari data.""")
	print("=" * 100)
	
def main():
	
	dict_budaya = dict()
	print()
	print("{:^100s}".format("BudayaKB Lite v2.0"))
	print("{:^100s}".format("Created by Farah Naz."))
	print("="*100)
	print("Selamat datang di sistem Budaya Knowledge Base. Silakan masukan perintah anda.")
	print("Untuk melihat semua perintah yang tersedia, ketik \"Bantuan\"")
	print("Untuk keluar dari BudayaKB Lite, ketik \"Keluar\"")
	print("="*100)
	try:
		user_input = input("Masukkan perintah: ").split(" ")	
		command = user_input[0].lower()

		parameter = user_input[1:]
		if type(parameter) == list:
			parameter = " ".join(user_input[1:])

		while command != "keluar":
			if command == "bantuan":
				bantuan()
			elif command == "impor":
				dict_budaya = impor(dict_budaya, parameter)
			elif command == "ekspor":
				ekspor(dict_budaya, parameter)
			elif command == "carinama":
				cari_nama(dict_budaya, parameter.lower())
			elif command == "caritipe":
				cari_tipe(dict_budaya, parameter.lower())
			elif command == "cariprov":
				cari_prov(dict_budaya, parameter.lower())
			elif command == "tambah":
				dict_budaya = tambah(dict_budaya, parameter)
			elif command == "update":
				dict_budaya = update(dict_budaya, parameter)
			elif command == "stat":
				stat(dict_budaya)
			elif command == "stattipe":
				stat_tipe(dict_budaya)
			elif command == "statprov":
				stat_prov(dict_budaya)
			elif command == "hapus":
				dict_budaya = hapus(dict_budaya, parameter)
			else:
				print("Perintah yang Anda masukkan tidak tersedia.\
				\nKetik \"Bantuan\" untuk melihat semua perintah yang tersedia.")

			print("."*50)
			user_input = input("Masukkan perintah : ").split(" ")	
			command = user_input[0].lower()

			parameter = user_input[1:]
			if type(parameter) == list:
				parameter = " ".join(user_input[1:])

		print("="*100)
		print("{:^100s}".format("~ Sampai jumpa! Jangan lupa untuk mencintai budaya Indonesia! ~"))
		print("{:^100s}".format("Keluar dari BudayaKB Lite v2.0 "))
		print("{:^100s}".format("Created by Farah Naz."))
		print("="*100)

	except KeyboardInterrupt:
		print("\nAnda menghentikan program dengan keyboard.")
		print("="*100)
		print("{:^100s}".format("~ Sampai jumpa! Jangan lupa untuk mencintai budaya Indonesia! ~"))
		print("{:^100s}".format("Keluar dari BudayaKB Lite v2.0 "))
		print("{:^100s}".format("Created by Farah Naz."))
		print("="*100)

if __name__ == "__main__":
	main()