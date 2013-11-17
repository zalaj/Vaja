import csv
file = open('vaja_podatki.csv', 'rt',encoding='ascii')
read = csv.reader(file)
rownum =0
##tukaj sem privzela, da je atrinut glede na katerega gledamo pogojno verjetnost
##vedno v zadnjim stolpcu

def discrete (read,slovar,atribut):
    #read je datoteka csv
    #slovar je slovar od kjer dobimo vrednosti atributa
    #atribut = atribut za katerega računamo verjetnosti
    atributi=list(slovar.keys())    ##seznam vseh atributov
    z_vr=slovar.get(atribut)        ##zaloga vrednosti za ta atribut
    p_yes=[0]*len(z_vr)
    p_no=[0]*len(z_vr)
    rownum=0
    for row in read:
        row=row[0].rsplit(';')
        if rownum ==0:
            header = row
            index = header.index(atribut)
        else:
            if row[len(atributi)-1]=='No':
                for i in range(0, len(z_vr)):
                    if row[index]==z_vr[i]:
                        p_no[i]=p_no[i]+1
            if row[len(atributi)-1]=='Yes':
                for i in range(0, len(z_vr)):
                    if row[index]==z_vr[i]:
                        p_yes[i]=p_yes[i]+1
        rownum=rownum+1
    frek_no=sum(p_no)
    frek_yes=sum(p_yes)
    for i in range (0,len(p_yes)):
        p_yes[i]=p_yes[i]/frek_yes
    for i in range (0,len(p_no)):
        p_no[i]=p_no[i]/frek_no
    return(p_yes, p_no)
