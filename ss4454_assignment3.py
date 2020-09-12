import sys
import random

#read data file

train_data = sys.argv[1]
file = open(train_data)

data= []
i=0

r= file.readline()

while(r!=''):
    a=r.split()
    b=len(a)
    r2=[]
    
    for j in range(0,b,1):
        r2.append(float(a[j]))
        if j== (b-1):
            r2.append(float(1))
    data.append(r2)
    r=file.readline()
    
rows= len(data)    
cols= len(data[0])

#print(r2)
#print(rows)
#print(cols)

file.close()

#read label data

labels= sys.argv[2]
file= open(labels)

trainlabels = {}
n=[]
n.append(0)
n.append(0)

r= file.readline()

while(r !=''):
    a= r.split()
    if int(a[0]) == 0:
        trainlabels[int(a[1])] = -1
    else:
        trainlabels[int(a[1])] = int(a[0])
    r= file.readline()
    n[int(a[0])] +=1

#print(trainlabels)

#initialize w

w=[]
for j in range(cols):
    w.append(0)
    w[j]= (0.02 * random.uniform(0,1)) - 0.01

#dot product
def dp(list1,list2):
    dp=0
    refw= list1
    refx= list2
    for j in range(cols):
        dp += refw[j]*refx[j]
    return dp

#gradient descent iteration
eta= 0.001

#error outside the loop

error= 0.0

for i in range(rows):
    if(trainlabels.get(i) != None):
        error += max(0, 1-trainlabels.get(i)*dp(w,data[i]))

#initialize flag and iteration parameters

flag=0
k=0

while(flag !=1):
    k+=1
    delf=[]
    for i in range(cols):
        delf.append(0)
    for i in range(rows):
        if(trainlabels.get(i) != None):
            d_p= dp(w,data[i])
            for j in range(cols):
                if(d_p*trainlabels.get(i)<1):
                    delf[j]+=-1*data[i][j]*trainlabels.get(i)
                else:
                    delf[j]+=0
    for j in range(cols):
        w[j]=w[j]-eta*delf[j]
    curr_error=0
    for i in range(rows):
        if(trainlabels.get(i)!= None):
            curr_error += max(0,1-trainlabels.get(i)*dp(w,data[i]))
        #print(error,k)
    if error-curr_error < 0.001:
            flag=1
    error= curr_error
#print(error)
#difference in error

#print("count",k)
#print("w=",w)

normw=0
for j in range((cols-1)):
    normw+= w[j]**2
    #print(w[j])

print("w = [",w[0],",",w[1],"]")
    
normw= (normw)**0.5
print("||w||   =    ",normw)
d_origin = w[(len(w)-1)]/normw
if (d_origin>0):
    print("Distance to origin = ",d_origin)
else:
    print("Distance to origin = ",-d_origin)

for i in range(rows):
    if(trainlabels.get(i) == None):
        d_p= dp(w,data[i])
        if(d_p>0):
            d_p=d_p
            #print("1   ",i)
        else:
            d_p=d_p
            #print("0   ",i)

        