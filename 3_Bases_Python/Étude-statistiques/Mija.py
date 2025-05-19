import statistics as stat
import math
import random
import matplotlib.pyplot as plt
import pandas
import statsmodels.api as smi

#Une fonction qui g�n�re deux listes de donn�es corr�l�es
def gener(n):
    x=[]
    y=[]
    k=0
    for _ in range(0,100):
        x.append(random.gauss(0,1))
        y.append(random.randint(-10,10)*x[k]+random.uniform(-4,4))
        k=k+1
    return (x,y)

#Une fonction qui �tudie les propri�t�s statistiques d'une liste
def statistika(x):
    medi=stat.median(x)
    mode=stat.mode(x)
    espe=stat.mean(x)
    vari=stat.variance(x)
    ectp=stat.stdev(x)
    return (medi,mode,espe,vari,ectp)

#la fonction main
n=int(input("Veuillez entrer la taille des deux listes que vous vouler  :"))
x,y=gener(n)
x_medi,x_mode,x_espe,x_vari,x_ectp=statistika(x)
y_medi,y_mode,y_espe,y_vari,y_ectp=statistika(y)
liste=['m�diane','mode','esp�rance','variance','�cart-type']
liste_x=[x_medi,x_mode,x_espe,x_vari,x_ectp]
liste_y=[y_medi,y_mode,y_espe,y_vari,y_ectp]
print("La covariance des deux donn�es vaut",stat.covariance(x,y))
print("Le coefficient de corr�lation des deux donn�es est de ", stat.correlation(x,y))
print("******Tableau r�capitulatifs de quelques propri�t�s statistiques des deux listes de donn�es******")
dataset=pandas.DataFrame({"Propri�t�s":liste,"x":liste_x,"y":liste_y})
dataset.head()
plt.title("Nuage de points")
plt.scatter(x,y,color="green")
#un tableau qui r�sume la regression lin�aire entre les deux listes
A=smi.add_constant(x)
model=smi.OLS(x,A)
results=model.fit()
print(results.summary())
import seaborn as sns
print("******Droite de regression lin�aire*****")
sns.regplot(x=x,y=y,ci=None,color="forestgreen")
liste_a=[x_espe,x_vari,x_ectp]
liste_b=[0,1,1]
lis=['esp�rance','variance','�cart-type']
print("******Tableau comparison des valeurs th�oriques et pratiques de la premi�re liste ******")
info=pandas.DataFrame({"Propri�t�s":lis,"T�ories":liste_b,"R�elles":liste_a})
info.head()
print("L'�sp�rance th�orique de la deuxi�me liste vaut 0,sa valeur r�eelle est",y_espe,".")

