st = 'miit'
print(st)
s=list(st)#converts the string to list
s[2]='e'#as list is mutable, change its value
del st
st = str(s)#now convert the list to str
print(st)