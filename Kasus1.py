# Muhammad Khairul Anamn
# A11.2019.11712

s = int(input('\nMasukkan jumlah detik : '))

def detikToJam(dtk):
    jam = dtk / 3600
    jamBulat = int(jam)
    return jamBulat

def detikToMenit(dtk):
    sisaMenit = dtk % 3600
    menit = sisaMenit / 60
    menitBulat = int(menit)
    return menitBulat

def detik(dtk):
    sisaDetik = dtk % 60
    return sisaDetik

def hasil(dtk):
    if dtk > 3600:
        print('Perjalanan anda jauh, siapkan perbekalan yang memadai')
    else:
        print('Perjalanan anda dekat, siapkan perbekalan yang secukupnya')

displayClock = print(detikToJam(s),'Jam', detikToMenit(s),'Menit', detik(s),'Detik')

displayClock
hasil(s)


