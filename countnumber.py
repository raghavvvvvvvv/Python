#wap to input number, find number of digits ina number and print ex: 1457
n=int(input('Enter a number '))
c=0
while n>0:
    r=n%10
    c+=1
    n=n//10
print(' number of digits are %d'%(c))