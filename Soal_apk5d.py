#cek nilai huruf
jwbulangprog = "y"
while jwbulangprog=="y" or jwbulangprog=="Y":
    print ("====================")
    print ("   CEK NILAI HURUF  ")
    print ("====================")
    n=1
    while int(n)>0 and int(n)<=100:
        n = input(">> Masukkan Nilai = ")
        #cek batasan inputan nilai 0-100
        if int(n)>0 and int(n)<=100:
            if int(n)>=91 and int(n)<=100: sts="A"
            elif int(n)>=81 and int(n)<=90: sts="B"
            elif int(n)>=71 and int(n)<=80: sts="C"
            else:
                sts="D"
            print (sts)

            jwbulangprog = input(">>> Ulang program? y/t = ")
            if jwbulangprog=="t" or jwbulangprog=="T":
                break
        else:
                pesan=">>> Masukkan nilai huruf 0-100 saja"
                print(pesan)
                break