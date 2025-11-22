with open(r"G:\sem-3\python_lab\lab13\a (1).tif",'rb')as f:
    binDT=f.read()
print(binDT)

with open("c.tif",'wb')as f:
    f.write(binDT)
    f.close()