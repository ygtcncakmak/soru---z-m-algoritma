
def digital_root(n):
    
    while (n > 10):
        birbas = n % 10
        onbas = int(((n % 100) - birbas)/10)
        yüzbas = int(((n % 1000) - (n % 100))/100)
        binbas = int(((n % 10000)-(n % 1000))/1000)
        onbinbas = int(((n % 100000)-(n % 10000))/10000)
        yüzbinbas = int(((n % 1000000)-(n % 100000))/100000)
        if n > 10 and n < 100:
            if n/10 > 0 and n % 10 < 10:
                print(f"{onbas},{birbas}")
                n = birbas+onbas
        if n > 100 and n < 1000:
            if n/100 > 0 and n % 100 < 100:
                print(f"{yüzbas},{onbas},{birbas}")
                n = birbas+onbas+yüzbas
        if n > 1000 and n < 10000:
            if n/1000 < 0 and n % 1000 < 1000:
                print(f"{binbas},{yüzbas},{onbas},{birbas}")
                n = birbas+onbas+yüzbas+binbas
        if n > 10000 and n <= 999999:
            print(f"{onbinbas},{binbas},{yüzbas},{onbas},{birbas}")
            n = birbas+onbas+yüzbas+binbas+onbinbas+yüzbinbas
    if n < 10:
        print(n)
    


digital_root(777777)
