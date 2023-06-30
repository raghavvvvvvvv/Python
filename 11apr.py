s = {43, 56, 78, 87}
s.add(100)
s.update({1,2,3,4})
print(s)
print(len(s))
s.remove(56)
print(s)
s.discard(43)
print(s)
s.discard(12) # removes the item if it doesn't exist won't rase the error
print(s)
s = set((0, 2, 3, 6, 8, 1))
print(s)
print(s.pop())
print(s)

