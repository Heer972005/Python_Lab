list1=[5,2,90,24,10]
list2=[6,3,91,25,12]
comb=list(zip(list1,list2)) 
print(comb)

for i in range(0,5):
    comb1=list1[i]+(list2[i])
    print(comb1)

'''print(list1[1::2],list2[1::2]=list2[1::2],list1[1::2])
print(list1[1::2],list2[1::2]=list2[1::2],list1[1::2])
print(list1[1::2],list2[1::2]=list2[1::2],list1[1::2])'''