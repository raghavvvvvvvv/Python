dic = {'studid': 1001, 'studname':'Rohit','Branch':'Cse'}
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())
print(len(dic))
print(dic.get('studname'))
print(dic.get('Branch'))
dic.pop('studname')
print(dic)
dic.popitem()
print(dic)