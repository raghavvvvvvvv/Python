# wap to input a number, find the factorial value of the number
num=int(input('Enter a number '))
f=1
while num>0:
    f=f*num
    num-=1
print('factorial value',f)