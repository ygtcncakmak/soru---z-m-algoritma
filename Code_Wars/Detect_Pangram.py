def is_pangram(s):
    s = str(s)
    s = s.lower()
    # web sitesinde ı harfini çıkarınca kabul ediyor
    alfabe = "abcdefghıijklmnopqrstuvwxyz"
    count = 0
    count2 = 0
    for i in alfabe:
        
        result = s.find(alfabe[count2])
        if result == 0:
            count += 1
        elif result == -1:
            break
        count2 += 1
    if count2 == len(alfabe):
        print("True")
        return True
    else:
        print("False")
        return False



is_pangram("The quick, brown fox jumps over the lazy dog!")
