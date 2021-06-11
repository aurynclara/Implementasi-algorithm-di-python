#cek nilai total transaksi beli printer
jwbulangprog = "y"
while jwbulangprog=="y" or jwbulangprog=="Y":
    print ("===================================================")
    print (" TOTAL BAYAR TRANSAKSI PEMBELIAN PRINTER EPSON T20 ")
    print ("===================================================")

    #Cek harga printer
    HargaPrinter = 660000
    MinDiskon = 1500000
    persenDiskon = 0.15
    TotalAwal = 0
    TotalBayar = 0

    #input Jumlah Beli
    JmlBeli = input ("Jumlah Printer Epson T20 yang dibeli = ")

    #nilai Diskon 
    NilaiDiskon = int(TotalAwal)*int(persenDiskon)

    #proses Hitung Total
    TotalAwal = int(HargaPrinter)*int(JmlBeli)
    NilaiDiskon = int(TotalAwal)*int(persenDiskon)
    TotalBayar = int(TotalAwal)-int(NilaiDiskon)

    #Tampil
    print("Total Transaksi Pembelian Printer Epson T20 = Rp " + str (TotalBayar))