#working methods of list
l1=[10,20,30]
print(l1)
l1.append(40)
print(l1)
print(l1.count(10))
print(l1.index(30))
l2=l1.copy()
print(l2)
l1.insert(2,33)
print(l1)
l1.remove(30)
print(l1)
l1.pop(3)
print(l1)
l3=[70,80,90]
print(l3)
print(l1)
l1.reverse()
print(l1)
l1.extend(l3)
print(l1)
l1.sort(reverse=True)
print(l1)
l1.pop()
print(l1)
l1.clear()
print(l1)
l1=['L','I','P']
print(l1)
del l1[1:4]
print(l1)
print(l1+l3)
print(l1*3)
print(len(l1))
del l1
#print(l1)
