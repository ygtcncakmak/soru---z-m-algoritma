def narcissistic(value):
    birbas = value % 10
    onbas = int(((value % 100) - birbas)/10)
    yüzbas = int(((value % 1000) - (value % 100))/100)
    binbas = int(((value % 10000)-(value % 1000))/1000)
    onbinbas = int(((value % 100000)-(value % 10000))/10000)
    yüzbinbas = int(((value % 1000000)-(value % 100000))/100000)
    
    if value/10 > 0 and value % 10 < 10:
        if (birbas**2)+(onbas**2) == value:
            print("True")
            return True

    if value > 100 and value < 1000:
        if value/100 > 0 and value % 100 < 100:
            if (birbas**3)+(onbas**3)+(yüzbas**3) == value:
                print("True")
                return True

    if value > 1000 and value < 10000:
        if value/1000 < 0 and value % 1000 < 1000:
            if (birbas**4)+(onbas**4)+(yüzbas**4)+(binbas**4) == value:
                print("True")
                return True
    if value > 10000 and value <= 99999:
        if (birbas**5)+(onbas**5)+(yüzbas**5)+(binbas**5)+(onbinbas**2) == value:
            print("True")
            return True
    else:
        print("False")
        return False
    if value< 10:
        print("True")
        return True
narcissistic(1652 )