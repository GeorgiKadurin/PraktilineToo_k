
#21 Запросите у пользователей несколько имен и выведите на экран более длинное и короткое имя.
from math import*
from random import*
    
s = float(input(""))
l = s.split()
 
lon = max(l, key=len)
short = min(l, key=len)
 
print(f'Longest: {lon}, shortest: {short}')
print()
print()

s = "Paariss numrid iesafws osfwkgmewwlk mf3eknekeffee "
l = s.split()
 
lon = max(l, key=len)
short = min(l, key=len)
 
print(f'Longest: {lon}, shortest: {short}')


#0 castom

while True:
    try:
        print("Tere Tulemast")
        print()
        print("Meil on sortimendis mitut tüüpi pitsasid")
        print()
        Neli_juustu=int(input("Pizza Neli juustu.(soovite-1 või ei soovi-0): "))
        Havai=      int(input("Pizza Havai.(soovite-1 või ei soovi-0):"))
        Margarita=  int(input("Pizza Margarita.(soovite-1 või ei soovi-0):"))
        Peperoni=   int(input("Pizza Peperoni.(soovite-1 või ei soovi-0):"))
        
        if Neli_juustu==1 and Havai==0 and Margarita==0 and Peperoni==0:
            Neli_juustu=10      #10
            Havai=0             #10.99
            Margarita=0         #11.30
            Peperoni=0          #12
            q=Neli_juustu+Havai+Margarita+Peperoni
            print("Ostu summa:",q )

        elif Neli_juustu==0 and Havai==1 and Margarita==0 and Peperoni==0:
            Neli_juustu=0       #10
            Havai=10.99         #10.99
            Margarita=0         #11.30
            Peperoni=0          #12
            w=Neli_juustu+Havai+Margarita+Peperoni
            print("Ostu summa:",w )

        elif Neli_juustu==0 and Havai==0 and Margarita==1 and Peperoni==0:
            Neli_juustu=0       #10
            Havai=0             #10.99
            Margarita=11.30     #11.30
            Peperoni=0          #12
            e=Neli_juustu+Havai+Margarita+Peperoni
            print("Ostu summa:",e )

        elif Neli_juustu==0 and Havai==0 and Margarita==0 and Peperoni==1:
            Neli_juustu=0       #10
            Havai=0             #10.99
            Margarita=0         #11.30
            Peperoni=12          #12
            r=Neli_juustu+Havai+Margarita+Peperoni
            print("Ostu summa:",r )

        elif Neli_juustu==1 and Havai==1 and Margarita==0 and Peperoni==0:
            Neli_juustu=10      #10
            Havai=10.99         #10.99
            Margarita=0         #11.30
            Peperoni=0          #12
            t=Neli_juustu+Havai+Margarita+Peperoni
            print("Ostu summa:",t )
         
        elif Neli_juustu==1 and Havai==0 and Margarita==1 and Peperoni==0:
            Neli_juustu=10       #10
            Havai=0            #10.99
            Margarita=11.30         #11.30
            Peperoni=0          #12
            y=Neli_juustu+Havai+Margarita+Peperoni
            print("Ostu summa:",y )

        elif Neli_juustu==1 and Havai==0 and Margarita==0 and Peperoni==1:
            Neli_juustu=10       #10
            Havai=0         #10.99
            Margarita=0         #11.30
            Peperoni=12          #12
            u=Neli_juustu+Havai+Margarita+Peperoni
            print("Ostu summa:",u )

        elif Neli_juustu==1 and Havai==1 and Margarita==1 and Peperoni==0:
            Neli_juustu=10      #10
            Havai=10.99         #10.99
            Margarita=11.30     #11.30
            Peperoni=0          #12
            i=Neli_juustu+Havai+Margarita+Peperoni
            print("Ostu summa:",i )

        elif Neli_juustu==1 and Havai==1 and Margarita==1 and Peperoni==1:
            Neli_juustu=10      #10
            Havai=10.99         #10.99
            Margarita=11.30     #11.30
            Peperoni=12          #12
            a=Neli_juustu+Havai+Margarita+Peperoni
            print("Ostu summa:",a )

        elif Neli_juustu==0 and Havai==1 and Margarita==1 and Peperoni==0:
            Neli_juustu=0      #10
            Havai=10.99         #10.99
            Margarita=11.30     #11.30
            Peperoni=0          #12
            s=Neli_juustu+Havai+Margarita+Peperoni
            print("Ostu summa:",s )

        elif Neli_juustu==0 and Havai==1 and Margarita==0 and Peperoni==1:
            Neli_juustu=10      #10
            Havai=10.99         #10.99
            Margarita=0         #11.30
            Peperoni=12          #12
            d=Neli_juustu+Havai+Margarita+Peperoni
            print("Ostu summa:",d )

        elif Neli_juustu==0 and Havai==1 and Margarita==1 and Peperoni==1:
            Neli_juustu=10      #10
            Havai=10.99         #10.99
            Margarita=11.30     #11.30
            Peperoni=0          #12
            h=Neli_juustu+Havai+Margarita+Peperoni
            print("Ostu summa: ",h )

        if Neli_juustu==0 and Havai==0 and Margarita==0 and Peperoni==0: 
            print("Te ei tellinud midagi. ")
            
        print()
        j=float(input("Mida soovite maksta kaardi või sularahaga: " ))
        l=float(input)("Anna raha.")
        if l==j: 
            print("Täname ostu eest")
        elif l<j:
            print(f"Üleandmine:{j-l}")
        else:
             print(f"Vaja rohkem maksta {j-l}")
            
    except:    
         print("")



       
def countSymbols(s):
    t=0
    for i in s:
        t+=1
    return t

items = ["Sisestaga nimi:"]

maxStr=""

for elem in items:
    if countSymbols(elem)>countSymbols(maxStr):
        maxStr=elem

print(maxStr)
print()
print()


a = input()
r2 = a
f2 = a
while a != "стоп":
    d = len(a)
    if d < len(r2):
        r2 = a
    if d > len(f2):
        f2 = a
    a = input()
if len(set(r2) - set(f2)):
    print('НЕТ')
else :
    print('ДА')

print()
print()




list = str(input()).split()

for i in list:
 print(i)

print("") 
print(list)

while True:
    s = input("Sisestage nimi: ").split()
    print(max(s, key=len))

    break



x = 0
while x==5:
    x=int(input("Sisestage nimi: "))
   
x += 1

list = str(input()).split()
print(max(list, key=len))



hui = input()
print(len([i for i in hui if i.isalpha()]))
print()
print()



# initialize string
bucket_list = 'J,a,p,a,n'

# comma delimiter
result = len(bucket_list.split(','))

# Prints an array of strings
print(bucket_list.split(','))

print("There are " + str(result) + " words.")
print()
print()


while True:
    name=input("Sisestage nimi: ")
    count=name.count("name")


x = 0
while x==5:
    x=int(input("Sisestage nimi: "))
   
x += 1

b = "ananas buy for mm" 
c = "buy for" 
count = b.count(c) # print count 
print("The count is:", count)