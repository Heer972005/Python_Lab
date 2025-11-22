list1=[[1,2],[3,4],[5,6],[7,8]]
lists=[item for List in list1 for item in List]
print(list1)
print(lists)
for i in list1:
    for j in i:
        print(j)