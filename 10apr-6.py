# create a new list - list comprehension
l1 = [2**x for x in range(10)]
print(l1)
l1 = [x for x in range(21,31)]
print(l1)
# code block equivalent to above
pow2=[]
for x in range(10):
    pow2.append(2**x)
print(pow2)
for x in range(21,31):
    pow2.append(x)
print(pow2)

