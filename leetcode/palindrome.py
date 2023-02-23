

def ikibamaklı(bir, on):
    if (bir == on):
        print("palindromik bir sayıdır")
    else:
        print("malesef palinromik sayı değil")


def ücbasamaklı(bir, yüz):
    if (bir == yüz):
        print("palindromik bir sayıdır")
    else:
        print("malesef palinromik sayı değil")


def dörtbasamaklı(bir, on, yüz, bin):
    if (bir == bin and on == yüz):
        print("palindromik bir sayıdır")
    else:
        print("malesef palinromik sayı değil")


def besbasamaklı(bir, on, yüz, bin, onbin):
    if (bir == onbin and on == bin):
        print("palindromik bir sayıdır")
    else:
        print("malesef palinromik sayı değil")


def altıbasamaklı(bir, on, yüz, bin, onbin, yüzbin):
    if (bir == yüzbin and on == onbin and yüz == bin):
        print("palindromik bir sayıdır")
    else:
        print("malesef palinromik sayı değil")


def yedibasamaklı(bir, on, yüz, onbin, yüzbin, milyon):
    if (bir == milyon and on == yüzbin and yüz == onbin):
        print("palindromik bir sayıdır")
    else:
        print("malesef palinromik sayı değil")


def sekizbasamaklı(bir, on, yüz, bin, onbin, yüzbin, milyon, onmilyon):
    if (bir == onmilyon and on == milyon and yüz == yüzbin and bin == onbin):
        print("palindromik bir sayıdır")
    else:
        print("malesef palinromik sayı değil")


def dokuzbasamaklı(bir, on, yüz, bin, yüzbin, milyon, onmilyon, yüzmilyon):
    if (bir == yüzmilyon and on == onmilyon and yüz == milyon and bin == yüzbin):
        print("palindromik bir sayıdır")
    else:
        print("malesef palinromik sayı değil")


def onbasamaklı(bir, on, yüz, bin, onbin, yüzbin, milyon, onmilyon, yüzmilyon, milyar):
    if (bir == milyar and on == yüzmilyon and yüz == onmilyon and bin == milyon and onbin == yüzbin):
        print("palindromik bir sayıdır")
    else:
        print("malesef palinromik sayı değil")


def palindrom(basamak, sayı):

    print(sayı)

    birler = sayı % 10
    onlar = int(((sayı % 100)-birler)/10)
    if (basamak == 2):
        ikibamaklı(birler, onlar)
    yüzler = int(((sayı % 1000)-(sayı % 100))/100)
    if (basamak == 3):
        ücbasamaklı(birler, yüzler)
    bin = int(((sayı % 10000)-int((sayı % 1000)))/1000)
    if (basamak == 4):
        dörtbasamaklı(birler, onlar, yüzler, bin)
    onbin = int(((sayı % 10000)-(sayı % 10000))/10000)
    if (basamak == 5):
        besbasamaklı(birler, onlar, yüzler, bin, onbin)
    yüzbin = int(((sayı % 100000)-(sayı % 10000))/100000)
    if (basamak == 6):
        altıbasamaklı(birler, onlar, yüzler, bin, onbin, yüzbin)
    milyon = int(((sayı % 1000000)-(sayı % 100000))/1000000)
    if (basamak == 7):
        yedibasamaklı(birler, onlar, yüzler, onbin, yüzbin, milyon)
    onmilyon = int(((sayı % 10000000)-(sayı % 1000000))/10000000)
    if (basamak == 8):
        sekizbasamaklı(birler, onlar, yüzler, bin,
                       onbin, yüzbin, milyon, onmilyon)
    yüzmilyon = int(((sayı % 100000000)-(sayı % 10000000))/100000000)
    if (basamak == 9):
        dokuzbasamaklı(birler, onlar, yüzler, bin, yüzbin, milyon, onmilyon)
    milyar = int(((sayı % 1000000000)-(sayı % 100000000))/1000000000)
    if (basamak == 10):
        onbasamaklı(birler, onlar, yüzler, bin, onbin, yüzbin,
                    milyon, onmilyon,  yüzmilyon, milyar)
    print(milyar)
    print(yüzmilyon)
    print(onmilyon)
    print(milyon)
    print(yüzbin)
    print(onbin)
    print(bin)
    print(yüzler)
    print(onlar)
    print(birler)

basamak = int(input("kaç basamaklı bir sayı gireceksiniz "))
sayı = int(input("bir tam sayı giriniz "))


palindrom(basamak, sayı)
