import os



def menuuser():
    from Control.Control_User import tampilan1
    print("")
    g = input("Apakah ingin Masuk ke menu user Y/N : ")
    if g == "Y":
        os.system('cls')
        tampilan1()
    else :
        exit()