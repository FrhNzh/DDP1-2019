#!/usr/bin/env python3
"""

TEMPLATE TP4 DDP1 Semester Gasal 2019/2020

Author: 
Ika Alfina (ika.alfina@cs.ui.ac.id)
Evi Yulianti (evi.yulianti@cs.ui.ac.id)
Meganingrum Arista Jiwanggi (meganingrum@cs.ui.ac.id)
Last update: 26 November 2019

edited by Farah Nazihah, 9 Nov 2019

"""
from budayaKB_model import BudayaItem, BudayaCollection
from flask import Flask, request, render_template
# from wtforms import Form, validators, TextField

app = Flask(__name__)
app.secret_key ="tp4"

#inisialisasi objek budayaData
databasefilename = ""
budayaData = BudayaCollection()


#merender tampilan default(index.html)
@app.route('/')
def index():
	return render_template("index.html")

# Bagian ini adalah implementasi fitur Impor Budaya, yaitu:
# - merender tampilan saat menu Impor Budaya diklik	
# - melakukan pemrosesan terhadap isian form setelah tombol "Import Data" diklik
# - menampilkan notifikasi bahwa data telah berhasil diimport 	
@app.route('/imporBudaya', methods=['GET', 'POST'])
def importData():
	if request.method == "GET":
		return render_template("imporBudaya.html")

	elif request.method == "POST":
		f = request.files['file']
		f.save(f.filename)
		file_name = f.filename
		global databasefilename
		databasefilename = file_name
		n_data = budayaData.importFromCSV(file_name)
		return render_template("imporBudaya.html", result=n_data, fname=f.filename)

@app.route('/cariBudaya', methods=['GET', 'POST'])
def cariBudaya():
	if request.method == 'GET':
		return render_template('cariBudaya.html')
	elif request.method == 'POST':
		category = request.form['category']
		budaya = request.form['budaya']
		listCari = []

		if category == 'nama':
			listCari = budayaData.cariByNama(budaya)
		elif category == 'tipe':
			listCari = budayaData.cariByTipe(budaya)
		elif category == 'prov':
			listCari = budayaData.cariByProv(budaya)

		return render_template('cariBudaya.html', result=listCari, kata_kunci=budaya, ketegori=category)

@app.route('/tambahBudaya', methods=['GET', 'POST'])
def tambahBudaya():
	global databasefilename
	budayaData.importFromCSV(databasefilename)
	if request.method == 'GET':
		return render_template('tambahBudaya.html')
	elif request.method == 'POST':
		nama = request.form['nama']
		tipe = request.form['tipe']
		prov = request.form['prov']
		ref = request.form['ref']
		hasil = budayaData.tambah(nama, tipe, prov, ref)

		budayaData.exportToCSV(databasefilename)
		return render_template("tambahBudaya.html", result=hasil, nama_budaya=nama)

@app.route('/ubahBudaya', methods=['GET', 'POST'])
def ubahBudaya():
	global databasefilename
	budayaData.importFromCSV(databasefilename)
	if request.method == 'GET':
		return render_template('ubahBudaya.html')
	elif request.method == 'POST':
		nama = request.form['nama']
		tipe = request.form['tipe']
		prov = request.form['prov']
		ref = request.form['ref']
		result = budayaData.ubah(nama, tipe, prov, ref)

		budayaData.exportToCSV(databasefilename)
		return render_template('ubahBudaya.html', result=result)
	
@app.route('/hapusBudaya', methods=['GET', 'POST'])
def hapusBudaya():
	global databasefilename
	budayaData.importFromCSV(databasefilename)
	if request.method == 'GET':
		return render_template('hapusBudaya.html')
	elif request.method == 'POST':
		nama = request.form['nama']
		hasil = budayaData.hapus(nama)

		budayaData.exportToCSV(databasefilename)
		return render_template('hapusBudaya.html', result=hasil)

@app.route('/statsBudaya', methods=['GET', 'POST'])
def statsBudaya():
	if request.method == 'GET':
		return render_template('statsBudaya.html')
	elif request.method == 'POST':
		category = request.form['category']
		dictStat = dict()
		count = budayaData.stat()
		if category == 'tipe':
			dictStat = budayaData.statByTipe()
		elif category == 'prov':
			dictStat = budayaData.statByProv()

		return render_template('statsBudaya.html', result=dictStat, counter=str(count), cat=category)

# run main app
if __name__ == "__main__":
	app.run(debug=True)