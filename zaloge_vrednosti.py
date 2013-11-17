##koda za pregled parametrov
import csv
file = open('vaja_podatki.csv', 'rt',encoding='ascii')
read = csv.reader(file)

def vrednosti(read):
    rownum = 0
    #zaloga je seznam v katerega so dodani podseznami zalog vrednosti vsakega atributa posebej
    zaloga=[]
    for row in read:
        row=row[0].rsplit(';')
        #header je seznam vseh atributov po imenut
        if rownum == 0:
            header=row      
        else:
            for column in range (0,len(header)):
                if rownum ==1:
                    zaloga.append([row[column]])
                else:
                    if row[column] not in zaloga[column]:
                        zaloga[column].append(row[column])         
        rownum=rownum+1
    #values je slovar: ključi so vsi atributi, vrednosti so zaloge vrednosti za vsak atribut
    values={}
    for i in range (0, len(header)):
        values[header[i]]=zaloga[i]
    return(values)

##metode ne slovarjihjih:
##list(x.keys()) - seznam vseh ključev
##list(x.values()) - seznav vseh vrednosti
##list(x.items()) - seznam vseh parov ključev in vrednsoti
