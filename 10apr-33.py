# map(): coverts an integer, string to list or tuple
# integer number to list
n=12345
lst = list(map(int,str(n)))
print(lst)
n='12345'
lst = list(map(int, n))
print(lst)
st='hyderabad'
lst = list(map(str, st))
print(lst)
#string to tuple
st='hyderabad'
tpl=tuple(map(str, st))
print(tpl)