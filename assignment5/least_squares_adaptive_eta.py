import sys
import random
import math

#dot product function

def dot_product(refw, refx, cols):
    dp=0
    for j in range(0, cols, 1):
        dp += refw[j]*refx[j]
    return dp

datafile = sys.argv[1]
f = open(datafile)
#l=line
data = []
i = 0
l = f.readline()

#reading data

while(l != ''):
    a = l.split()
    alen = len(a)
    l2 = []
    for j in range(0, alen, 1):
        l2.append(float(a[j]))
        if j == (alen-1) :
            l2.append(float(1))
    data.append(l2)
    l = f.readline()

rows = len(data)
cols = len(data[0])
f.close()

#reading labels

labelfile = sys.argv[2]
f = open(labelfile)
class_var = {}
class_size = []
class_size.append(0)
class_size.append(0)
l = f.readline()

while(l != ''):
    a = l.split()
    if int(a[0]) == 0:
        class_var[int(a[1])] = -1
    else:
        class_var[int(a[1])] = int(a[0])
    l = f.readline()
    class_size[int(a[0])] += 1

#initializing w

w = []

for j in range(0, cols, 1):
    w.append(0)
    w[j] = (0.02 * random.uniform(0,1)) - 0.01

w1 = []

    
#Gradient Descent Iteration

#eta = 0.0001
error = 0.0

#computng error

for i in range(0, rows, 1):
    if (class_var.get(i) != None):
        error += (-class_var.get(i) + dot_product(w, data[i], cols))**2

temp = 0
c=0

#computing dellf
#updating w
#computing new error
besteta=0.0

while(temp != 1):
    c += 1
    dellf = []
    for j in range(0,cols,1):
        dellf.append(0)
    for i in range(0, rows, 1):
            if class_var.get(i) != None:
                dp = dot_product(w, data[i], cols)
                for j in range(0, cols, 1):
                    dellf[j] += ((-class_var.get(i) + dp)*data[i][j])
	
    eta_list = [1, .1, .01, .001, .0001, .00001, .000001, .0000001, .00000001, .000000001, .0000000001, .00000000001 ]
    
    bestobj = 1000000000000
	
    for k in range(0,len(eta_list),1):
        eta=eta_list[k]
        w1=w
        for j in range(0, cols, 1):
                w1[j] = w1[j] - eta*dellf[j]        
        #new_error1 = 0
        for i in range(0, rows, 1):
            if (class_var.get(i) != None):
                new_error1 += (-class_var.get(i) + dot_product(w1, data[i], cols))**2
        if new_error1 < bestobj:
            besteta=eta
            bestobj = new_error1
           
    
    for j in range(0, cols, 1):
        w[j] = w[j] - besteta*dellf[j]
    #new_error = 0
    for i in range(0, rows, 1):
            if (class_var.get(i) != None):
                new_error += (-class_var.get(i) + dot_product(w, data[i], cols))**2
            
    #print ("error is = ",error, c)
    if (error - new_error) < 0.001:
        temp = 1
    error = new_error

#print("count = ",c)
#print("w = ",w)

#prediction
print("bestobj = ",bestobj)
print("besteta = ",besteta)

for i in range(0, rows, 1):
    if (class_var.get(i) == None):
        dp = dot_product(w, data[i], cols)
        #print ("dp is",dp)
        if(dp>0):
            print("1 ",i)
        else:
            print("0 ",i)

