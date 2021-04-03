
import math
def fx(x):
    F=x**3-x
    return(F)
def gx(x):
    G=x**2
    return(G)

X1=int(input("donner un nombre X1 "))
print("X1= ",X1)
X2=int(input("donner un nombre X2 "))
print("X2= ",X2)
pas=int(input("donner un nombre de pas "))
print(" le nombre de pas selectionner est ",pas,"cm")
if X1>X2:    # utilisation de cette condition pour ne pas avoir des problemes au niveau de l'interval donnée
    temp=X1
    X1=X2
    X2=temp
#cette boucle a pour but de calculer le nombre des points d'intersection entre les deux fonctions en rapport avec le pas donnée
k=0
for i in range(X1,X2,pas):
    if fx(i)==gx(i):
        k=k+1
        res=i
        print("intersection ",k,"= ",'(',res,',',fx(i),')')
if k==0:
    print("dans cet interval donnée il n'y a pas de point d'intercection")
elif k>0:
    print("dans cet interval donnée il y'a ",k," point d'intersection ")

S=0
for i in range(X1,X2,pas):
    S=S+(i-(i-1))*(math.fabs(fx(i)-gx(i)))
print("la superficie est ",S,"cm²")

