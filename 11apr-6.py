a = {1,2,3,4,5}
print(a)
b = {4,5,6,7,8}
print(b)
print(a,b)
print(b,a)
# union operator
print(b | a)
print(a.union(b))
print(b.union(a))
# intersection operator
print(a&b)
print(a.intersection(b))
print(b.intersection(a))
# difference operator
print(a-b)
print(a.difference(b))
print(b.difference(a))
# symmetric difference
print(a^b)
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
