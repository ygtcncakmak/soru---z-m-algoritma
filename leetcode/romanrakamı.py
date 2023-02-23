dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
sayi = input("roman rakamlarını giriniz :  ").upper()

chardizi = list(sayi)

büyüksayi = 0
büyükstr = ""
index=0

i = 0

while i < len(sayi):
    if büyüksayi < dict[chardizi[i]]:
        büyükstr = chardizi[i]
        büyüksayi = dict[chardizi[i]]
        index=i
    i = i+1
print("en büyük sayi : ",büyüksayi)
print("en büyük STR : ",büyükstr)
cıkarılacak=0
toplanacak=0

j=0
while j < len(chardizi[0:index]):
    cıkarılacak+=dict[chardizi[j]]
    
    j=j+1
k=0
while k < len(chardizi[index:len(chardizi)-1]):
    toplanacak+=dict[chardizi[k]]
    k=k+1
print("sonuç : ",toplanacak-cıkarılacak)
