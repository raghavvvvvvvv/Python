# coding logic to search fopr an element in the list
l1 = [1, 3, 4, 6, 8, 10, 11, 56, 77]
n = int(input(' input search element '))
# using for loop to search for an element
f = 0
for ele in l1:
    if ele == n:
        f = 1
        break
if f == 1:
    print(n, ' is found ')
else:
    print(n, 'is not found')
