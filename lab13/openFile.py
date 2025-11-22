'''file1=open("G:\\sem-3\\python_lab\\lab13\\ict.txt")
#file1=open(r"G:\sem-3\python_lab\lab13\ict.txt")
for i in file1:
    print (i)
print (file1.read())
'''

with open("G:\sem-3\python_lab\lab13\ict.txt",'r') as f1:
    dt=f1.read()
    print(dt)

f1=open(r"G:\sem-3\python_lab\lab13\ict.txt",'r')
print(f1.read(5))


with open("G:\sem-3\python_lab\lab13\ict.txt",'r') as file:
    dt=file.readlines()
    for i in dt:
        word=i.split()
        print(word)
