import random
import sys
file_train = sys.argv[1]
file_test = sys.argv[2]

#-----------------------------Read-Data-------------------------------
first_label=[]
test_array = []
with open(file_train) as my_file:
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

weight=random.randint(-2,2)
weight=[weight]*max_index
#print weight

weight=map(int,weight)
weight1=weight
weight1=map(int,weight1)
weight2=weight
weight2=map(int,weight2)
weight3=weight
weight3=map(int,weight3)
weight4=weight
weight4=map(int,weight4)

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
bias_glob=random.randint(-2,2)
bias=bias_glob
#print bias
j=0
c=0
first_label=map(int,first_label)
for i in final_result:
    i=map(int,i)
    #print i
    A=map(lambda x,y:x*y,weight1,i)
    B=reduce(lambda x,y:x+y,A)
    #print A, "this is A"
    #print B, "this is B"
    derived=B+bias
    #print derived, "dhdihdi"
    if (derived*first_label[j])<=0:
        D=map (lambda x:x*first_label[j],i)
        weight1=map(lambda x,y:x+y,weight1,D)
        bias=bias+first_label[j]
        #print B, "Thsi is B"
        #print first_label[j], "ojojojojojo"
        #print bias, "new bias"
        #print weight, "weight"
        c=c+1
    j=j+1
#weight_train_simple = weight + [0]
weight_train_simple=weight1
print "TRAIN"
print "this is simple perceptron"
#print weight_train_simple, "this is new weight vector"
#print len(weight_train_simple)
print c, "this is number of mistakes"
#del weight[(len(weight)-1)]

#------------------------------Margin P-----------------------------
#print type(weight),"weight",type(final_result)

u=input ("what is margin?, between 0 and 5 \n")
bias=bias_glob
j=0
c=0
first_label=map(int,first_label)
for i in final_result:
    i=map(int,i)
    #print i
    A=map(lambda x,y:x*y,weight2,i)
    B=reduce(lambda x,y:x+y,A)
    #print A, "this is A"
    #print B, "this is B"
    derived=B+bias
    #print derived, "dhdihdi"
    if (derived*first_label[j])<=u:
        D=map (lambda x:x*first_label[j],i)
        weight2=map(lambda x,y:x+y,weight2,D)
        bias=bias+first_label[j]
        #print B, "Thsi is B"
        #print first_label[j], "ojojojojojo"
        #print bias, "new bias"
        #print weight, "weight"
        c=c+1
    j=j+1
#weight = weight +[0]
print "TRAIN"
print "this is margin perceptron"
weight_train_margin=weight2
#print weight_train_margin, "this is new weight vector"
#print len(weight_train_margin)
print c, "this is number of mistakes"
#----------------------TEST DATA-----------------------------------
#------------------------------------------------------------------


#-----------------------------Read-Data-------------------------------
first_label_test=[]
test_array_test = []
with open(file_test) as my_file:
    for line in my_file:
        line=line.lower()
        line = line.split()
        test_array_test.append(line[1:])
        first_label_test.append(line[0])
Total_rows_test=len(test_array_test)
#print Total_rows
"""for i in test_array:
    print i"""
#print max(test_array)

#-------------------------Store last array element-------------------
labels_test=[]
for line in test_array_test: 
    labels_test.append(line[-1])
#print labels

#print first_label

indexes_test=[]
for i in labels_test:
    
    i=i.split(':')
    index=int(i[0])
    indexes_test.append(index)
max_index_test=max(indexes_test)+1
#print max_index_test
#print max_index

#---------------------Weight + Data Array----------------------------
weight_test=[]
weight_test=[0]*max_index_test
weight_test =map(int,weight_test)
#print weight

data_test=[[0]*max_index_test for i in range(Total_rows_test)]

#-------------------Assigning values in data array-------------------
final_result_test=[]
for h in test_array_test:
    #print h,"@@@@@@@"
    foobar_test=[0 for i in range(max_index_test)]
    #print len(foobar)
    for item in h:
        item=item.split(':')
        index=int(item[0])
        value=int(item[1])
        foobar_test[index]=value
    final_result_test.append(foobar_test)


"""for i in final_result[0:5]:
    print i"""
#1--------------------------------------------------------------------
#print type(weight),"weight",type(final_result)
bias=bias_glob
true=0
false=0
j=0
c=0
first_label=map(int,first_label)
#print first_label_test[0:10]
for i in final_result:
    i=map(int,i)
    #print i
    A=map(lambda x,y:x*y,weight_train_simple,i)
    B=reduce(lambda x,y:x+y,A)
    #print A, "this is A"
    #print B, "this is B"
    derived=B+bias
    #print derived_test, "dhdihdi"
    if (derived*first_label[j])>0:
        true=true+1
    else:
        false=false+1
        c=c+1
    j=j+1
print "TRAIN Accuracy-----Simple Perceptron"
#print "this is simple perceptron"
#print weight_test, "this is new weight vector"
#print c, "this is number of mistakes"
accuracy = float(true)/(true+false)
print accuracy, "this is accuracy"
weight_train_simple=weight_train_simple+[0]




#2--------------------------------------------------------------------
#print type(weight),"weight",type(final_result)
bias=bias_glob
true=0
false=0
j=0
c=0
first_label=map(int,first_label)
#print weight_train_margin
#print first_label_test[0:10]
for i in final_result:
    i=map(int,i)
    #print i
    A=map(lambda x,y:x*y,weight2,i)
    B=reduce(lambda x,y:x+y,A)
    #print A, "this is A"
    #print B, "this is B"
    derived=B+bias
    #print derived_test, "dhdihdi"
    if (derived*first_label[j])>0:
        true=true+1
    else:
        false=false+1
        c=c+1
    j=j+1
print "TRAIN Accuracy Margin Perceptron"
#print weight_test, "this is new weight vector"
#print c, "this is number of mistakes"
accuracy = float(true)/(true+false)
print accuracy, "this is accuracy"
weight_train_margin=weight_train_margin+[0]







#------------------------Multiply-------------------------------------
#print type(weight),"weight",type(final_result)
bias=bias_glob
true=0
false=0
j=0
c=0
first_label_test=map(int,first_label_test)
#print first_label_test[0:10]
for i in final_result_test:
    i=map(int,i)
    #print i
    A=map(lambda x,y:x*y,weight_train_simple,i)
    B=reduce(lambda x,y:x+y,A)
    #print A, "this is A"
    #print B, "this is B"
    derived_test=B+bias
    #print derived_test, "dhdihdi"
    if (derived_test*first_label_test[j])>0:
        true=true+1
    else:
        false=false+1
        c=c+1
    j=j+1
print "TEST Accuracy-----Simple Perceptron"
#print "this is simple perceptron"
#print weight_test, "this is new weight vector"
#print c, "this is number of mistakes"
accuracy = float(true)/(true+false)
print accuracy, "this is accuracy"

#------------------------------Margin P-----------------------------
#print type(weight),"weight",type(final_result)

#u=input ("what is u?, between 0 and 5 \n")
bias=bias_glob
j=0
true=0
false=0
c=0
first_label_test=map(int,first_label_test)
for i in final_result_test:
    i=map(int,i)
    #print i
    A=map(lambda x,y:x*y,weight_train_margin,i)
    B=reduce(lambda x,y:x+y,A)
    #print A, "this is A"
    #print B, "this is B"
    derived_test=B+bias
    #print derived, "dhdihdi"
    if (derived_test*first_label_test[j])>0:
        true=true+1
    else:
        false=false+1
        c=c+1
    j=j+1
print "TEST Accuracy Margin Perceptron"
#print "this is margin perceptron"
#print weight_test, "this is new weight vector"
#print c, "this is number of mistakes"
accuracy = float (true)/(true+false)
print accuracy, "this is accuracy"



