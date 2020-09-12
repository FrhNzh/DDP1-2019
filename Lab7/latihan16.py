n_cat = int(input('Banyaknya kucing yang hadir: '))

all_cat = {}

for i in range(n_cat):					# mengelompokkan kucing berdasarkan angkatan
	temp = input().split(' ')
	name_cat, year_cat = temp

	if year_cat in all_cat:
		lst = all_cat[year_cat]
		lst.append(name_cat)
		all_cat[year_cat] = lst
	else:
		all_cat[year_cat] = [name_cat]


for x, y in all_cat.items():
	print(x + ":", y)