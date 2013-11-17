##koda za pregled parametrov
import csv
file = open('vaja_podatki.csv', 'rt',encoding='ascii')
read = csv.reader(file)

def argument(read):
    rownum = 0
    zaloga=[]
    for row in read:
        row=row[0].rsplit(';')
        if rownum == 0:
            header=row
        else:
            for i in range (0,len(header)):
                if rownum ==1:
                    zaloga.append([row[i]])
                else:
                    if row[i] not in zaloga[i]:
                        zaloga[i].append(row[i])         
        rownum=rownum+1
    slovar={}
    for i in range (0, len(header)):
        slovar[header[i]]=zaloga[i]
    return(slovar)
