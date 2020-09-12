import math
from sys import exit
import sys
from array import array

datafile = sys.argv[1]
f=open(datafile)
data=[]

l=f.readline()
while (l != ''):
    k=l.split()
    l2=[]
    for j in range(0, len(k), 1):
        l2.append(int(k[j]))
    
    data.append(l2)
    l=f.readline()
rows=len(data)
cols =len(data[0])
f.close()

#read train labels
labelfile = sys.argv[2]
f=open(labelfile)
trainlabels= []
l=f.readline()
while(l != ''):
    k=l.split()
    trainlabels.append(int(k[0]))
    l=f.readline()
f.close()


testfile = sys.argv[3]
f=open(testfile)
testdata=[]

l=f.readline()
while (l != ''):
    k=l.split()
    l2=[]
    for j in range(0, len(k), 1):
        l2.append(int(k[j]))
    
    testdata.append(l2)
    l=f.readline()
f.close()


def feature_select(data, trainlabels):
    chisqlist = []
    for j in range(0, len(data[0]),1):
	    observed = [[1,1],[1,1],[1,1]]    
	    for i in range(0, len(data),1):
	        if trainlabels[i] == 0:
	            if data[i][j] == 0:
	                observed[0][0] += 1
	            elif data[i][j] == 1:
	                observed[1][0] += 1
	            elif data[i][j] == 2:
	                observed[2][0] += 1
	        elif trainlabels[i] == 1:
	            if data[i][j] == 0:
	                observed[0][1] += 1
	            elif data[i][j] == 1:
	                observed[1][1] += 1
	            elif data[i][j] == 2:
	                observed[2][1] += 1
	    #print("observed",observed)
	    coll = [ sum(x) for x in observed]
	    #print("colss",colss)
	    roww = [ sum(x) for x in zip(*observed) ]
	    #print("rowss",rowss)
	    total = sum(coll)
	    #print("total",total)
	    expected = [[(row*col)/total for row in roww] for col in coll]
	    #print("expected",expected)
	    chisq = [[((observed[i][j] - expected[i][j])**2)/expected[i][j] for j in range(0,len(expected[0]),1)] for i in range(0,len(expected),1)]
	    #print("chisq",chisq)
	    final_chisq = sum([sum(x) for x in zip(*chisq)])
	    #print("final_chisq",final_chisq)
	    chisqlist.append(final_chisq)
    #print("chisqlist",chisqlist)
    chi_sort = sorted(range(len(chisqlist)), key=chisqlist.__getitem__, reverse=True)
    index = chi_sort[:15]
    return index


def redu_data(data, column_no):
	reduc_data = []
	l1 = list(zip(*data))
	for j in column_no:
		reduc_data.append(l1[j])
	reduc_data = list(zip(*reduc_data))
	return reduc_data
	
column_no = feature_select(data, trainlabels)
#print("The selected feature columns are:")
#print(column_no)
featur_file=open("featur.txt",mode="w",encoding="utf-8")

for i in range(0, len(column_no),1):
    st=str(column_no[i])
    featur_file.write(st + "\n")

reduc_data=redu_data(data, column_no)
reduc_testdata=redu_data(testdata, column_no)

from sklearn import svm
clf = svm.SVC(kernel='rbf', C = 1.0, gamma=0.001)
clf.fit(reduc_data,trainlabels)
predic_list=clf.predict(reduc_testdata)
predic_file=open("prediclabels.txt",mode="w",encoding="utf-8")
print("Finished writing to prediclabels.txt")
for i in range(0, len(predic_list),1):    
    stt=str(predic_list[i])+" "+str(i)
    predic_file.write(stt + "\n")
    


exit()
