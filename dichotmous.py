import matplotlib.pyplot as plt
import random
import numpy as np


def plot(coeff,xl,xr,type):
    x = np.linspace(-20, 20, 200)
    plt.plot(x,objective(coeff,x))  # the graph
    plt.plot(xl,objective(coeff,xl),"hm",ms="15") #initial left point
    plt.plot(xr,objective(coeff,xr),"hm",ms="15") #initial right point
    iter=20
    f=open("dichotomous_calculated_data.txt","w")

    for i in range(iter):  #total of 15 iteraitions
        delta=(xr-xl)/iter
        mid=(xl+xr)/2
        x2=mid+delta/2  #right side
        x1=mid-delta/2 #left side
        y1=objective(coeff,x1)
        y2=objective(coeff,x2)
        txt=str((i+1))+"th iterarion"
        f.write(txt)
        txt="\nXl = "+str(xl)+"\nXr = "+str(xr)+""
        f.write(txt)
        txt="\nx1 = "+str(x1)+"\nx2 = "+str(x2)
        f.write(txt)
        txt="\nf(x1) = "+str(y1)+"\nf(x2) = "+str(y2)+"\n"
        f.write(txt)        
        plt.plot(x2,y2,"ob",ms="8")  #the right point
        plt.plot(x1,y1,"*b",ms="8")  #the left point
        if(type == 1):
            if(y1>y2):
                xl=x1
                f.write("f(x1) > f(x2)\n\n")
            else:
                xr=x2
                f.write("f(x1) < f(x2)\n\n")
        elif(type == 2):            
            if(y1>y2):
                xr=x2
                f.write("f(x1) > f(x2)\n\n")
            else:
                xl=x1           
                f.write("f(x1) < f(x2)\n\n") 

    finalx=(xl+xr)/2
    finaly=objective(coeff,finalx)
    plt.plot(finalx,finaly,"sy",ms="15")
    f.close()
    plt.show()
    

def objective(coeff,val):
    #start=float(input("enter start "))    
    sum=0
    for i in range(len(coeff)):
        sum=sum+(coeff[i]*(val**i))
    return sum 




n=int(input("enter the degree of function = "))
coeff=[]
for i in range(n+1):
    print("Enter coeff of x^",i ," = ",end="")
    c=float(input())
    coeff.append(float(c))

type=int(input("Enter 1. minimisation 2. maximisation (1/2))= "))
xl=-5
#random.randint(-20,20)  #random xl left
xr=random.randint(xl,20)  #random xr right
print(" xl initial = ",xl)
print(" xr initial = ",xr)
#delta=float(input("Enter the delta value = "))
plot(coeff,xl,xr,type)       # i have set delta to be xl-xr / total iterations

