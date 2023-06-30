#program to search for an element in a list
l1=[10,20,30,40]
n=int(input(' input search element '))
if n in l1:
    print(n," is found at ",l1.index(n),"postion")
else:
    print(n, " is not found")