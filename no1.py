angka = ["","satu","dua","tiga","empat","lima","enam",
        "tujuh","delapan","sembilan"]
def terbilang(n) :
    if n < 10 :
        return angka[n]
    elif n >= 1000000000 :
        return terbilang(n // 1000000000) + ' milyar ' + terbilang(n % 1000000000) if n % 1_000000000 != 0 else ''
    elif n >= 1000000 :
        return terbilang(n // 1000000) + ' juta ' + terbilang(n % 1000000) if n % 1000000 != 0 else ''
    elif n >= 1000 :
        if n // 1000 == 1 :
            return " seribu " + terbilang(n % 1000) if n % 1000 != 0 else ''
        else :
            return terbilang(n // 1000) + ' ribu ' + terbilang(n % 1000) if n % 1000 != 0 else ''
    elif n == 100 :
        return 'seratus'
    elif n >= 100 :
        if n // 100 == 1 :
            return " seratus " + terbilang(n % 100) if n % 100 != 0 else ''
        else:
            return terbilang(n // 100) + ' ratus ' + terbilang(n % 100) if n % 100 != 0 else ''
    elif n >= 20 :
        return terbilang(n // 10) + ' puluh ' + terbilang(n % 10) if n % 10 != 0 else ''
    else:
        if n == 10:
            return ' sepuluh'
        elif n == 11:
            return ' sebelas'
        else:
            return terbilang(n % 10) + ' belas'

n = input('input ? ')
a = str(n).split(".")
awal = int(a[0])
akhir = int(a[-1])
if "." not in n :
    print(f'{n:} = {terbilang(awal)}')
elif "."  in n :
    print(n,":",terbilang(awal) ,'koma',terbilang(akhir))