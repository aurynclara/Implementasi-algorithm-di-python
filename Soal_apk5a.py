#cek kelulusan, jika nilai >60 maka status lulus
jwb = "y"
while jwb=="y" or jwb=="Y":
    print ("==================")
    print (" CEK KELULUSAN  ")
    print ("==================")
    #setiap value yang diinputkan, secara default bertipe data STRING
    n = input(">> Masukkan Nilai = ")
    #cek nilai
    if int(n)>60:
        sts = "LULUS"
    else:
        sts="ULANG"
    print(sts)

    #inputan untuk break
    jwb = input(">> Mulai lagi ? y/t = ")
    if jwb== "t" or jwb =="T":
        break