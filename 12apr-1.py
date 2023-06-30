def add(instanceof,*args):
    if instanceof == 'int':
        result = ''
    if instanceof == 'str':
        result = ''
    if instanceof == 'welcome':
        result = ''
    print(type(args))
    for i in args:
        result = result + i

    return result
print(add('int',3,4,5))
print(add('str','I','am','in','Jammu'))
print(add('welcome','to','python'))