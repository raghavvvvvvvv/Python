# tuple --tuple is ordered and indexed sequence of data elements
#it is immutable object
#insertion  oreder is preserved
#heterogeneous elements are allowed
#tuple supports both + and - indexing
#the elements can be mutable
#how to create tuples
#example:
#creating an empty tuple
tpl=()
print(tuple(tpl))
#creating an empty tuple using tuple constructor method
tpl=tuple()
print(tuple(tpl))
tpl=(10,20,30)
print(type(tpl))
tpl=10,20,30
print(type(tpl))
tpl=(100)
print(type(tpl))
tpl=(100,)
print(type(tpl))