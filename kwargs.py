def myFun(arg1, **kwargs):
    for key, value in kwargs.items():
        print('%s %s %s'%(arg1, key, value))
myFun("hi", first = 'Model Institute', mid = 'of', last = 'Emgineering')
print('%s %s %s' % (arg1, key, value))
