# Muhammad Khairul Anamn
# A11.2019.11712

import sys

print('==========================================================================')
print('==|     Judul Film     |               Bioskop jam 12.30               |==')
print('==|                    |_______________________________________________|==')
print('==|                    | Citra XXI(1)  |  E Plaza(2)   |  Cinemaxx(3)  |==')
print('==|____________________|_______________|_______________|_______________|==')
print('==| Susi Susanti(s)    | 40 ribu       | 25 ribu       | 35 ribu       |==')
print('==| Maleficent 3D(m)   | 50 ribu       | 35 ribu       | 45 ribu       |==')
print('==========================================================================')
print('__________________________________________________________________________')
inFilm = str(input('\nJudul film yang dipilih(s/m): '))
inBioskop = int(input('Bioskop yang dipilih(1-3): '))
inJmlTiket = int(input('Jumlah tiket: '))

def verifikasi(film, bioskop):
    verFilm = (film == 's' or film == 'm')
    kedua = (verFilm == False and bioskop > 3)
    if kedua == True:
        print('Maaf, bioskop dan film yang anda pilih tidak ditemukan')
        sys.exit()
    elif verFilm == False:
        print('Maaf, film yang anda pilih tidak ditemukan')
        sys.exit()
    elif bioskop > 3:
        print('Maaf, bioskop yang anda pilih tidak ditemukan')
        sys.exit()

def hargaFilm(film):
    if film == 's':
        harga = [0, 40000, 25000, 35000]
    elif film == 'm':
        harga = [0, 50000, 35000, 45000]
    return harga

def diskon(tot):
    if tot < 100000:    
        dis = 0
    elif tot < 200000:
        dis = tot*5/100
    elif tot >= 200000:
        dis = tot*10/100
    return int(dis)

verifikasi(inFilm, inBioskop)
harga = hargaFilm(inFilm)[inBioskop] * inJmlTiket
total = harga - diskon(harga)

print('__________________________________________________________________________')
print('\nHarga  =', 'Rp', harga)
print('Diskon =', 'Rp', diskon(harga))
print('____________________+')
print('Total  =', 'Rp', total)
