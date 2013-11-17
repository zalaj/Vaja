##koda za pregled parametrov
import csv
file = open('vaja_podatki.csv', 'rt',encoding='ascii')
read = csv.reader(file)

def argument(read):
    rownum = 0
    #zaloga je seznam v katerega so dodani podseznami zalog vrednosti vsakega atributa posebej
    zaloga=[]
    for row in read:
        row=row[0].rsplit(';')
        #header je seznam vseh atributov po imenut
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
    #slovar je slovar: ključi so vsi atributi, vrednosti so zaloge vrednosti za vsak atribut
    slovar={}
    for i in range (0, len(header)):
        slovar[header[i]]=zaloga[i]
    return(slovar)

##metode ne slovarjih:
##list(x.keys()) - seznam vseh ključev
##list(x.values()) - seznav vseh vrednosti
##list(x.items()) - seznam vseh parov ključev in vrednsoti
