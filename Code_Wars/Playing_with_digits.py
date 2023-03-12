def dig_pow(n, p):
    birbas = n % 10
    onbas = int(((n % 100) - birbas)/10)
    yüzbas = int(((n % 1000) - (n % 100))/100)
    binbas = int(((n % 10000)-(n % 1000))/1000)
    onbinbas = int(((n % 100000)-(n % 10000))/10000)
    yüzbinbas = int(((n % 1000000)-(n % 100000))/100000)

    if n < 10:
        result = (birbas**p)/n
        if result*n == (birbas**p):
            print(n)
            print(result)
            return result
        else:
            print(n)
            print(result)
            return result

    if n > 10 and n < 100:
        if n/10 > 0 and n % 10 < 10:
            result = ((birbas**(p+1))+(onbas**(p)))/n

        if result*n == (birbas**(p+1))+(onbas**(p)):
            print(n)
            print(result)
            return result
        else:
            print(n)
            print(result)
            return -1

    if n > 100 and n < 1000:
        if n/100 > 0 and n % 100 < 100:
            result = ((birbas**(p+2))+(onbas**(p+1))+(yüzbas**p))/n
            if result*n == (birbas**(p+2))+(onbas**(p+1))+(yüzbas**p):
                print(f"{n} , {p}")
                print(result)
                return result
            else:
                print(f"{n} , {p}")
                print(result)
                return -1

    if n > 1000 and n < 10000:
        if n/1000 < 0 and n % 1000 < 1000:
            result = ((birbas**(p+3)) + (onbas**(p+2)) +
                      (yüzbas**(p+1)) + (binbas**p)) / n

            if result*n == (birbas**(p+3))+(onbas**(p+2)) + (yüzbas**(p+1))+(binbas**p):
                print(f"{n} , {p}")
                print(result)
                return result
            else:
                print(f"{n} , {p}")
                print(result)
                return -1
    if n > 10000 and n <= 99999:
        result = ((birbas**(p+4)) + (onbas**(p+3)) + (yüzbas**(p+2)) +
                  (binbas**(p+1)) + (onbinbas**p)) / n

        if result*n == (birbas**(p+4)) + (onbas**(p+3)) + (yüzbas**(p+2)) + (binbas**(p+1)) + (onbinbas**p):
            
            print(f"{n} , {p}")
            print(result)
            return result
        else:
            print(f"{n} , {p}")
            print(result)
            return -1


dig_pow(23783, 5)
