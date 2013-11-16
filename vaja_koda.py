###Testna koda za vajo

###najprej preberemo podatke
import csv
import math

#podatki
file = open('vaja_podatki.csv', 'rt',encoding='ascii')
read = csv.reader(file)
rownum =0
totalrows = len(open('vaja_podatki.csv').readlines())


#naštejemo atribute - sedaj jih naredim še ročno
x=['No','Married','120']       #to je tisti razred, za katerega delamo napoved
owner=['No', 'Yes']
status = ['Single','Married', 'Divorced']
razred=['No', 'Yes']            #končni razred
s=[]
o=[]

####for row in read:
##    row=row[0].rsplit(';')
##    if row[0] not in s:
##        s.append(row[0])

#vektroji frekvenc
p= [0]*len(razred)*len(owner)      
q= [0]*len(razred)*len(status)
mean=[0]*len(razred)
sd=[0]*len(razred)
yes=0
no=0
for row in read:
    row=row[0].rsplit(';')
    if rownum ==0: ar = row         #argumenti 
    #pogojne verjetnosti za No
    if row[3]==razred[0]:
        mean = 0
        sd
        no = no+1
        #home owner
        if row[0]==owner[0]: p[0]=p[0]+1
        else : p[1]=p[1]+1
        #status
        if row[1]==status[0]: q[0]=q[0]+1
        if row[1]==status[1]: q[1]=q[1]+1
        if row[1]==status[2]: q[2]=q[2]+1
        #income
    #pogojne verjetnosti za Yes
    if row[3]==razred[1]:
        yes=yes+1
        #home owner
        if row[0]==owner[0]: p[2]=p[2]+1
        else : p[3]=p[3]+1
        #status
        if row[1]==status[0]: q[3]=q[3]+1
        if row[1]==status[1]: q[4]=q[4]+1
        if row[1]==status[2]: q[5]=q[5]+1
    rownum = rownum + 1
for i in (0,len(owner)-1):
    p[i]=p[i]/no
for i in (len(owner),2*len(owner)-1):
    p[i]=p[i]/yes
for i in (0,len(status)-1):
    q[i]=q[i]/no
for i in (len(status),2*len(status)-1):
    q[i]=q[i]/yes
##    #z=zvezno(2,read, x[2])
file.close()

