# meminta input user
n = int(input('berhitung sampai '))

# loop untuk mengecek input
for i in range(n-1):
    angka = int(input())
    if angka != i+1:
        hilang = i+1

print('Angka yang hilang adalah', hilang)