import csv
import math
file = open('vaja_podatki.csv', 'rt',encoding='ascii')
read = csv.reader(file)
rownum =0
totalrows = len(open('vaja_podatki.csv').readlines())

#naštejemo atribute - sedaj jih naredim še ročno
x=['No','Married','120K']       #to je tisti razred, za katerega delamo napoved
owner=['No', 'Yes']
status = ['Single','Married', 'Divorced']
razred=['No', 'Yes']            #končni razred


##########################
####FUNKCIJA ZA NOTMALNO VERJETNOST
##########################
def zvezno(stolpec, datoteka, X):
    ###X je vrednost, za katero se računa verjetnost
    no=[]
    yes=[]
    for row in datoteka:
        row=row[0].rsplit(';')
        if row[3]==razred[0]:
            no.append(int(row[stolpec]))
        if row[3]==razred[1]:
            yes.append(int(row[stolpec]))
    mean_no=sum(no)/len(no)
    mean_yes = sum(yes)/len(yes)
    sd_no =[]
    sd_yes=[]
    for i in no:
        sd_no.append((i-mean_no)**2)
    for i in yes:
        sd_yes.append((i-mean_yes)**2)
    sd_no=sum(sd_no)/(len(no)-1)
    sd_yes=sum(sd_yes)/(len(yes)-1)
    p_yes= 1/(math.sqrt(2*math.pi*sd_yes))*math.exp(-(X-mean_yes)**2/(2*sd_yes))
    p_no= 1/(math.sqrt(2*math.pi*sd_no))*math.exp(-(X-mean_no)**2/(2*sd_no))
    return([p_yes, p_no])
  
