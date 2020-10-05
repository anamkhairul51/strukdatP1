# Muhammad Khairul Anam
# A11.2019.11712
# A11.4315

angka = int(input('Masukkan Angka: '))

for i in range(1, angka):
    if angka % i == 0:
        print(i)
    else:
        if angka != 1:
            print(',')
        else:
            i = i-1

