def cetakGambar(number):
    if type(number) != int:
        print ("Masukkan bilangan bernilain integer")
    else :
        cek = isOdd(number)
        nilaitengah = (number+1)/2
        if cek == True:
            for i in range(number):
                for j in range(number):
                    if ( j == 0 or j == number-1 or i == nilaitengah-1):
                        print("*", end = ' ')
                    else:
                        print("=", end = ' ')
                print()
        else:
            print ("Bukan bilangan ganjil")

def isOdd(number):
    if number % 2 == 0:
        return False
    else:
        return True
    
cetakGambar(5)