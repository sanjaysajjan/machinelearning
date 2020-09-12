import sys
import random
import math

#read data file

train_data=sys.argv[1]
file = open (train_data)

data = []

i = 0
r = file.readline()

while(r != '') : #read
    a= r.split()
    b= len(a)
    r2 = []
    for j in range(0, b, 1):
        r2.append(float(a[j]))
        if j == (b-1):
            r2.append(float(1))
        #data.append(r2)
    data.append(r2)
    r = file.readline()

rows = len(data)
cols = len(data[0])

file.close()

#read label data
labels=sys.argv[2]
file = open(labels)

trainlabels = {}

n = []
n.append(0)
n.append(0)

r = file.readline()

while(r != '') : #read
    a = r.split()
    trainlabels[int(a[1])] = int(a[0])
    r = file.readline()
    n[int(a[0])] += 1

#print(trainlabels)

#initialize w

w = []
for j in range(cols):
    w.append(0)
    w[j] = (0.02 * random.uniform(-0.01, 0.01))

##define function dot_product

def dotproduct(refw, refx, cols):
    dp = 0
    for j in range (0, cols, 1):
        dp += refw[j] * refx[j]
    return dp

datafile = sys.argv[1]
f = open(datafile)

i = 0
l = file.readline()

##gradient descent iteration

eta = 0.01
k = 1
c = 0

##calculate error outside the loop
error=0.0
for i in range (0, rows, 1):
        if(trainlabels.get(i) != None):
                dp = dotproduct(w, data[i], cols)
                sigm = 1/(1 + math.exp(-1 * dp))
                error += (-trainlabels.get(i) * math.log(sigm))-((1 - trainlabels.get(i)) * (math.log(sigm*(math.exp(-1*dp)))))

prev_error = error

while(abs(k)>0.001): #for sample data 0.0000001
	dellf = []
	for j in range(0,cols,1):
		dellf.append(0)
                                                             
	#Compute Dellf
	k = 0
	for i in range(0, rows, 1):
		if (trainlabels.get(i) != None):
			dp = dotproduct(w, data[i], cols)
			sigm = 1/(1+math.exp(-1*dp))
			for j in range(0,cols,1):
				dellf[j] += ((trainlabels.get(i)-(sigm))*data[i][j])

	#Update W
	for j in range(0, cols, 1):
		w[j] += eta*dellf[j]

	#Compute Error New
	error = 0
	for i in range(0,rows,1):
		if trainlabels.get(i)!=None:
			dp = dotproduct(w, data[i], cols)
			sigfn = 1/(1+math.exp(-1*dp))
			error += (-trainlabels.get(i)*math.log(sigm))-((1-trainlabels.get(i))*math.log(sigm*(math.exp(-1*dp))))	

	c += 1
	#print ("error is = ",error, c)
	k = error - prev_error
	prev_error = error

normw = 0
for j in range(0, cols-1, 1):
    normw += normw + (w[j]**2)
    #print(w[j])
print("\n")
normw = normw**(1/2)
print("||w||=", normw)
d_origin = w[(len(w)-1)]/normw
print("W0=",w[len(w)-1])

## Distance calculation
print("Distance to origin: ",abs(d_origin),"\n")
## Prediction

for i in range(rows):
    if(trainlabels[i] == None):
        d_p = dotproduct(w, data[i], cols)
        if(d_p > 0):
            print("1  ",i)
        else:
            print("0  ",i)
