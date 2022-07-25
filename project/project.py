import numpy as np
import math
import matplotlib.pyplot as plt
global inputs
inputs=[]
def setXandY(inputsFile):
    with open(inputsFile,"r")as iF:
        n=int(iF.readline())   #window int
        X=[]
        lenInputs=0
        while(True):#reading inputFile 
            lenInputs+=1
            try:
                a=float(iF.readline())
                inputs.append(a)
            except:
                break
            
        if(n!=1):
            m=(lenInputs-n)/(n-1)-1
        else:
            m=lenInputs
        i=m
        index=0
        X=[]
        Y=[] 
        while(i!=0):
            x=[]
            for j in range(0,n+1):
                if(j==0):
                    if(i!=m):
                        Y.append([inputs[index+1]])
                    x.append(1)
                elif(j==1):
                    x.append(inputs[index])
                else:
                    if(m<=index):
                        break
                    index+=1
                    x.append(inputs[index])
                    if(i==1):
                        Y.append([inputs[index+1]])
            X.append(x)
            i-=1

        with open("X.txt","w")as xF:
            xF.write(str(X))
            
        with open("Y.txt","w")as yF:
            yF.write(str(Y))
            
    return X,Y

def findW(inputsFile):
    X,Y=setXandY(inputsFile)
    x=np.array(X)
    y=np.array(Y)
    xT=x.transpose()
    try:
        W=np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(x),x)),np.transpose(x)),y)
        with open("W.txt","w")as wF:
            wF.write(str(W))
    except:
       print("W could not be found!!!!!")
    return W ,X,Y
    
def next_y(W,x,y,inputsFile):
    with open(inputsFile,"r")as iF:
        n=int(iF.readline())   #window int  
    currentX=inputs[len(inputs)-n-1:]#next row: contanins last x== xn == y[-1] ||||  [1,xn-1,xn]
    currentX[0]=1
    xx=np.array(currentX)
    nextY=np.dot(xx,W)
    return nextY
def norm(w,x,y):
    result=np.dot(x,w)-y
    norm1=0
    norm2=0
    for item in result:
        norm2+=result[0]**2
        norm1+=abs(result[0])
    return norm1 , math.sqrt(norm2)

def main():
    inputsFile=input("please enter inputs file name:")
    W,x,y=findW(inputsFile)
    nextY=next_y(W,x,y,inputsFile)
    print("the Predicted output is:", *nextY)
    norm1,norm2=norm(np.array(W),np.array(x),np.array(y))
    print("norm1 is:",*norm1)
    print("norm2 is:",norm2)

    fig, (ax1, ax2) = plt.subplots(2)
    ax2.plot(y)
    ax1.plot(np.dot(x,W))
    plt.show()

main()
