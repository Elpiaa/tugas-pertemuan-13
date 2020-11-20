def terbilang(n) :
    angka = ["","one","two","three","four","five","six",
             "seven","eight","nine","ten"]
    if n < 10 :
        return angka[n]
    elif n >= 1000000000 :
        return terbilang(n // 1000000000) + ' billion ' + terbilang(n % 1000000000) if n % 1_000000000 != 0 else ''
    elif n >= 1000000 :
        return terbilang(n // 1000000) + ' million ' + terbilang(n % 1000000) if n % 1000000 != 0 else ''
    elif n >= 1000 :
        if n // 1000 == 1 :
            return " one thousand " + terbilang(n % 1000) if n % 1000 != 0 else ''
        else :
            return terbilang(n // 1000) + ' thousand ' + terbilang(n % 1000) if n % 1000 != 0 else ''
    elif n >= 100 :
        if n // 100 == 1 :
            return " one hundred " + terbilang(n % 100) if n % 100 != 0 else ''
        else:
            return terbilang(n // 100) + ' hundred ' + terbilang(n % 100) if n % 100 != 0 else ''
    elif n >= 20 :
        if n//10 == 2 :
            return "twenty" + terbilang(n%10)
        elif n//10 == 3 :
            return "thirty "+terbilang(n%10)
        elif n//10 == 4 :
            return "forty "+terbilang(n%10)
        elif n//10 == 5 :
            return "fifty "+terbilang(n%10)
        elif n//10 == 8 :
            return "eighty "+terbilang(n%10)
        else :
            return terbilang(n // 10) + 'ty' + terbilang(n%10) if n%10 != 0   else ''
    else:
        if n == 10:
            return ' ten'
        elif n == 11:
            return ' eleven'
        elif n == 12 :
            return 'twelve'
        else:
            return terbilang(n % 10) + 'teen'

n = input('input ? ')
a = str(n).split(".")
awal = int(a[0])
akhir = int(a[-1])
if "." not in n :
    print(f'{n:} = {terbilang(awal)}')
elif "."  in n :
    print(n,":",terbilang(awal) ,'point',terbilang(akhir))