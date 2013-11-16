##Testna koda za vajo

##najprej preberemo podatke
import csv
file = open('vaja_podatki.csv', 'rt',encoding='ascii')
read = csv.reader(file)
i =0
n = nrows(read)
for row in read:
	row=row[0].rsplit(';')          
	if (i==0):st_atributov=len(row)

	
print(st_atributov)

          
