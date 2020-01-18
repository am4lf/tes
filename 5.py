def buatDeret(x,y):
    cek = cekBesarKecil(x,y)
    if cek == True:
        listAngka = []
        while True:
            if len(listAngka) == 0:
                listAngka.append(y)
            elif len(listAngka) == 1:
                deret = (y**2) % x
                listAngka.append(deret)
                temp_ax = deret
                temp_x = x
            elif len(listAngka) >= 2:
                temp_x = temp_x + 1
                deret = (temp_ax**2) % (temp_x)
                if (deret == 1) or (deret == 0):
                    listAngka.append(deret)
                    break
                else:
                    listAngka.append(deret)
                    temp_ax = deret
        print ("array : ", listAngka)
        print ("count : ", len(listAngka))
    else:
        print("Nilai x lebih kecil dari y")
    
def cekBesarKecil(x,y):
    if x > y:
        return True
    else:
        return False
    
buatDeret(16,5)