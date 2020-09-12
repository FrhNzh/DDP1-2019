# program untuk menghitung frekuensi kata


# mengimport module
import string
import numpy as np
import matplotlib.pyplot as plt

def textInput():
	"""Fungsi untuk meminta input dari user"""

	print("=" * 50)
	print("Masukan pesan: (untuk berhenti tekan enter.)")
	print("=" * 50)
	pesan = input("Pesan: ")
	semuaPesan = ""
	while pesan != "":							# meminta input terus-menerus
		semuaPesan += pesan + ' '
		pesan = input("Pesan: ")
	semuaPesan = semuaPesan.lower()						# mengubah teks menjadi huruf kecil seluruhnya

	return semuaPesan


def removePunc(text):
	"""Fungsi untuk menghapus tanda baca"""
	
	listFromText = []

	for word in text.split():
		word = word.strip(string.punctuation)                           # menghapus tanda baca dalam teks
		listFromText.append(word)

	return listFromText
		

def stopWord(text):
	"""Fungsi untuk menghapus kata-kata penghubung"""

	text = removePunc(text)                                                 # memanggil fungsi untuk menghapus tanda baca
	
	file = open('TP2-stopword.txt', 'r')				        # membuka file stopword
	stopWord = file.read().split()

	for word in text:					        	# menghapus stopword dalam teks
		if word in stopWord:
			text.remove(word)

	file.close()

	return text


def countWords(text):
	"""Fungsi untuk menghitung frekuensi kata"""

	listOfWord = []
	listOfFrequency = []

	for word in text:					        	# menghitung frekuensi kata
                if word == '':
                        pass
                elif word not in listOfWord:					# menyimpan kata ke dalam list
                        listOfWord.append(word)
                        listOfFrequency.append(1)
                else:
                        index = listOfWord.index(word)
                        listOfFrequency[index] = listOfFrequency[index] + 1     # menambah frekuensi kata yang sudah ada


	lst = [listOfWord, listOfFrequency]

	return lst


def drawTable(listOfWord, listOfFrequency):
	"""Fungsi untuk membuat tabel frekuensi"""

	print("Distribusi frekuensi kata: ")				        # judul di atas tabel
	print('-' * 40)
	print('{:3s} {:25s} {:10s}'.format('No.', 'Kata', 'Frekuensi'))
	print('-' * 40)

	number = 0								# penomoran poin di dalam tabel
	indexCounter = 0									
	for word in listOfWord:							# mencetak isi tabel
		number += 1
		print('{:3d} {:26s} {:<9d}'.format(number, word, listOfFrequency[indexCounter]))
		indexCounter += 1

	print('-' * 40)


def barGraph(listOfWord, listOfFrequency):
	"""Fungsi untuk menggambar grafik"""

	index = np.arange(len(listOfWord))

	plt.title("Frekuensi Kemunculan Kata")
	plt.barh(index, listOfFrequency)
	plt.xlabel('Frekuensi')
	plt.yticks(index, listOfWord, fontsize=6)

	plt.show()


def main():
	text = textInput()						        # meminta user memasukan pesan
	modifiedText = stopWord(text)					        # menghapus tanda baca dan kata hubung
	listOfWord, listOfFrequency = countWords(modifiedText)

	print(listOfWord,listOfFrequency)
	drawTable(listOfWord, listOfFrequency)

	listOfWord = listOfWord[::-1]
	listOfFrequency = listOfFrequency[::-1]				        # memanggil fungsi untuk membuat tabel
	barGraph(listOfWord, listOfFrequency)				        # memanggil fungsi untuk menggambar grafik

if __name__ == "__main__":
    main()
