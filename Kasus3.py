# Muhammad Khairul Anamn
# A11.2019.11712

nilai = int(input('Masukkan nilai anda: '))

if nilai <= 60:
    remidi = 'Test Ulang'
elif nilai < 70:
    remidi = 'Penugasan'
else:
    remidi = 'Tidak Ada'

print(remidi)