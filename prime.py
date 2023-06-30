#wap to check whether a number is prime or not
num=int(input('Enter a number '))
i=1
c=0
while i<=num:
    if num%i==0:
        c+=1
    i+=1
if c==2:
    print('%d is a prime number'%(num))
else:
    print('%d is not a prime number'%(num))