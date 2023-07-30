l1=['a','b','c','d','r','y']
print(l1)
print()
#******* using clone ******
print("using clone:")
y=l1[:]
y[2]=13
print(y)

print()
#******* using copy ********
print("using copy:")
x=l1.copy()
x[1]="Payal"
print(x)