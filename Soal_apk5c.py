#cek nilai
jwbulangprog = "y"
while jwbulangprog=="y" or jwbulangprog=="Y":
    print ("================")
    print ("    CEK NILAI   ")
    print ("================")
    n=1
    while int(n)>0 and int(n)<=100:
        n = input(">> Masukkan Nilai = ")
        #cek batasan nilai 0-100
        if int(n)>0 and int(n)<=100:
            if int(n)>80: sts="Baik Sekali"
            elif int(n)>=65: sts="Baik"
            elif int(n)>=55: sts="Cukup"
            elif int(n)>=40: sts="Kurang"
            else:
                sts="Kurang Sekali"
            print (sts)

            jwbulangprog = input(">>> Ulang program? y/t = ")
            if jwbulangprog=="t" or jwbulangprog=="T":
                break
        else:
            pesan=">>> Masukkan nilai 0-100 saja"
            print(pesan)