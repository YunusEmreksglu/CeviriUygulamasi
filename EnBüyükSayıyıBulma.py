def Bsayi(sayi1,sayi2):
    Sayi=["",""]
    if (sayi1>sayi2):
        Sayi=[sayi1,sayi2]
    if(sayi1<sayi2):
        Sayi=[sayi2,sayi1]

    return Sayi
print(Bsayi(2,2)[0])