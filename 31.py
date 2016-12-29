import sys
file_table2 = sys.argv[1]

#-----------------------------Read-Data-------------------------------
first_label=[]
test_array = []
with open(file_table2) as my_file:
    for line in my_file:
        line=line.lower()
        line = line.split()
        test_array.append(line[1:])
        first_label.append(line[0])
Total_rows=len(test_array)
#print Total_rows
"""for i in test_array:
    print i"""
#print max(test_array)

#-------------------------Store last array element-------------------
labels=[]
for line in test_array: 
    labels.append(line[-1])
#print labels

#print first_label

indexes=[]
for i in labels:
    
    i=i.split(':')
    index=int(i[0])
    indexes.append(index)
max_index=max(indexes)+1
#print max_index

#---------------------Weight + Data Array----------------------------
weight=[]
weight=[0]*max_index
weight =map(int,weight)
#print weight

data=[[0]*max_index for i in range(Total_rows)]

#-------------------Assigning values in data array-------------------
final_result=[]
for h in test_array:
    #print h,"@@@@@@@"
    foobar=[0 for i in range(max_index)]
    #print len(foobar)
    for item in h:
        item=item.split(':')
        index=int(item[0])
        value=int(item[1])
        foobar[index]=value
    final_result.append(foobar)


"""for i in final_result[0:5]:
    print i"""

#------------------------Multiply-------------------------------------
#print type(weight),"weight",type(final_result)
bias=0
j=0
c=0
first_label=map(int,first_label)
for i in final_result:
    i=map(int,i)
    #print i
    A=map(lambda x,y:x*y,weight,i)
    B=reduce(lambda x,y:x+y,A)
    #print A, "this is A"
    #print B, "this is B"
    derived=B+bias
    #print derived, "dhdihdi"
    if (derived*first_label[j])<=0:
        D=map (lambda x:x*first_label[j],i)
        weight=map(lambda x,y:x+y,weight,D)
        bias=bias+first_label[j]
        #print B, "Thsi is B"
        #print first_label[j], "ojojojojojo"
        #print bias, "new bias"
        #print weight, "weight"
        c=c+1
    j=j+1
print weight, "this is new weight vector"
print c, "this is number of mistakes"

#----------------Taking bias and next step----------------------------




