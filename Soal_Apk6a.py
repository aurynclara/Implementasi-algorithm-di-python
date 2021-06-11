#cek transaksi beli printer
print ("=======================================")
print (" TRANSAKSI PEMBELIAN PRINTER EPSON T20 ")
print ("=======================================")

#nilai awal variabel JmlBeli = Harga 1 Printer
HargaPrinter = 660000

#input Jumlah Beli
JmlBeli = input ("Jumlah Printer Epson T20 yang dibeli = ")

#proses Hitung Total
Total = int(HargaPrinter)*int(JmlBeli)

#Tampil
print("Total Transaksi Pembelian Printer Epson T20 = Rp " + str (Total))
