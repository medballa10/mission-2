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
if X1>X2:   # utilisation de cette condition pour ne pas avoir des problemes au niveau de l'interval donnée
    temp=X1
    X1=X2
    X2=temp
S=0
for i in range(X1,X2+1,pas):
    S=S+((math.fabs(fx(i)-gx(i))+math.fabs(fx(i-1)-gx(i-1)))/2)*pas
print("la superficie est = ",S,"cm²")