def second_symbol(s, symbol):
    s = str(s)
    count = 0
    for i in range(0, len(s)):
        if s[i] == symbol:
            count += 1
        if count == 2:
            print(i)
            return i
            break
    if count < 2:
        print(-1)
        return -1