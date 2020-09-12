#Write a Python program that determines the column with the
#best split for the CART decision tree algorithm. You don't
#have to write the CART algorithm in its entirety. You just
#have to write a program that will traverse all columns in the
#data and output the column and the threshold that gives the
#lowest gini index.
#___________________________________________________________________________

#Python Standard Modules
import sys

print("_____________________________________________________________________________________________________________\n")
# To accept Data file from Datasets
dataset_file = sys.argv[1]
f = open(dataset_file)

data = []
l = f.readline()

while(l != ''):
	a = l.split()
	alen = len(a)
	l2 = []
	for j in range(0, alen, 1):
		l2.append(float(a[j]))
	data.append(l2)
	l = f.readline()

rows = len(data)
cols = len(data[0])
f.close()

# To accept Training label file from Datasets
trainlabel_file = sys.argv[2]
f = open(trainlabel_file)
trainlabels = {}
class_size = []
class_size.append(0)
class_size.append(0)
l = f.readline()

while(l != ''):
	a = l.split()
	trainlabels[int(a[1])] = int(a[0])
	class_size[int(a[0])] = class_size[int(a[0])] + 1
	l = f.readline()
f.close()


list_gini = []
split = 0
templ = [0, 0]
for j in range(0, cols, 1):
    list_gini.append(templ)
temp = 0
column = 0

for j in range(0, cols, 1):

    listcolumn = [item[j] for item in data]
    keys = sorted(range(len(listcolumn)), key=lambda k: listcolumn[k])
    listcolumn.sort()
    # TO DISPLAY SORTED COLUMN LIST and KEYS, PLEASE "UNCOMMENT" "THE" "BELOW" "4 (FOUR)" "LINES"
    #print("___________________________\n")
    #print("\n SORTED COLUMN LIST \n",listcolumn)
    #print("___________________________\n")
    #print("\n KEYS \n",keys)
    gini_val = []
    previous_gini = 0
    previous_row = 0
    for k in range(1, rows, 1):

        lsize = k
        rsize = rows - k
        lp = 0
        rp = 0

        for l in range(0, k, 1):
            if (trainlabels.get(keys[l]) == 0):
                lp += 1
        for r in range(k, rows, 1):
            if (trainlabels.get(keys[r]) == 0):
                rp += 1
        gini = (lsize / rows) * (lp / lsize) * (1 - lp / lsize) + (rsize / rows) * (rp / rsize) * (1 - rp / rsize)
        gini_val.append(gini)

        previous_gini = min(gini_val)
        if (gini_val[k - 1] == float(previous_gini)):
            list_gini[j][0] = gini_val[k - 1]
            list_gini[j][1] = k
    if (j == 0):
        temp = list_gini[j][0]
    if (list_gini[j][0] <= temp):
        temp = list_gini[j][0]
        column = j
        split = list_gini[j][1]
        if (split != 0):
            split = (listcolumn[split] + listcolumn[split - 1]) / 2

print("_______________________________\n")
print("  GINI: ", temp, "\n  COLUMN: ", column, "\n  SPLIT: ", split)
print("_______________________________\n")
print("_____________________________________________________________________________________________________________\n")
