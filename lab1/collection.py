#lists,tuples,dictionaries,sets
list1=[123,567,89]
print(list1)

list2=["hello","how","are"]
print(list2)

list3=["hey","123","hello"]
print(list3)

list4=["apple","mango",123,345]
list5=["grapes"]
print(list4+list5)

print("\n\nDictionaries")
dict1={"comp":"computer","sci":"science"}
print(dict1["comp"])
dict2={"123":"computer","456":"maths"}
print(dict2["123"])
print(dict1["comp"]+dict2["123"])
#print(dict1+dict2)--type error
#print(dict1["computer"]+dict2["computer"])--key error

print("\n\nSets")
my_set={1,2,3,4,5}
print(my_set)

set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set1+set2)