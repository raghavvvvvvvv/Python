# coding logic for counting the frequency of a number in the list using for loop
l1 = [1, 2, 3, 4, 1, 5, 7, 8]
c = 0
n = int(input('enter an element to search '))
for ele in l1:
    if ele == n:
        c += 1
print(n, ' is found ', c, 'times')