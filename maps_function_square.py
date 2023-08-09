
y=[]
n=int(input("enter number of element"))
for i in range(n):
    y.append(int(input("enter elements")))
print("enter list is")
print(y)
print("triple the element of the list")
def abc(x):
    return x*3
print(list(map(abc, y)))