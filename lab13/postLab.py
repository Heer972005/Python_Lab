file=r"G:\sem-3\python_lab\lab13\ict.txt"

#a
with open(file,'r') as f:
    txt=f.read()
with open(file,'r') as f:
    line=f.readlines()

lines=len(line)
words=len(txt.split())
chrs=len(txt)

print("No. of Lines:",lines)
print("No. of words:",words)
print("No. of chrs:",chrs)

#b
list=[]
with open(file,'r') as f:
    for i in f:
        list.append(i.strip())#if not strip-['ICT ICT ICT\n', 'ICT ICT ICT ICT ICT']
print(list)

#c
import csv
with open("G:\sem-3\python_lab\lab13\data-1.csv",'r') as f:
    reader=csv.reader(f)
    for i in reader:
        print(i)

#d
file1="G:\sem-3\python_lab\lab13\ict.txt"
file2="G:\sem-3\python_lab\lab13\ict2.txt"
merged="merged.txt"
with open(file1,'r') as f1,open(file2,'r') as f2,open(merged,'w') as m:
    m.write(f1.read())
    m.write("\n")
    m.write(f2.read())
    #m.write("\n",f2.read())#type error-can take only 1 argument
print("merged:")