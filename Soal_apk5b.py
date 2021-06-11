#cek golongan usia
jwbulangprog = "y"
while jwbulangprog=="y" or jwbulangprog=="Y":
    print ("====================")
    print (" CEK GOLONGAN USIA  ")
    print ("====================")
    u=1
    while int(u)>0 and int(u)<=100:
        u = input(">> Masukkan Usia = ")
        #cek batasan inputan usia 0-100
        if int(u)>=0 and int(u)<=100:
            if int(u)>=60: sts="Lansia"
            elif int(u)>=35: sts="Dewasa"
            elif int(u)>=18: sts="Pemuda"
            elif int(u)>=15: sts="Remaja"
            else:
                sts="Anak"
            print(sts)

            jwbulangprog = input(">> Ulang program? y/t = ")
            if jwbulangprog=="t" or jwbulangprog=="T":
                break
        else:
            pesan=">>> Masukkan angka usia 0-100 saja"
            print(pesan)
            break