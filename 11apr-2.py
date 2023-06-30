#iteratingf through a set:

for letter in set ("apple"):
    print(letter, end=" ")
print('\n')
for char in set('aaaa'):
    print(char)
print('\n')
st="Roose"
s=set((st))
print(s)
print('\n')
st="Roose"
s={i for i in s} #creating a set from a string
print(s)
print('\n')
#creating a set from a list
lst=[1,2,3,54,66]
s={i for i in lst} #creating a set from a list
print(s)
print('\n')
lst=[43, 56, 34, 77]
d={i: i*i for i in lst}
print(d)
print('\n')

