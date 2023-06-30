#a positive integer is called a spy number if the sum and product of it is digits are equal.
#wap to input a number, find whether it is spy num or not
n=int(input('enter number '))
s=0
p=1
while n>0:
    digit=n%10
    s+=digit
    p*=digit
    n=n//10
if s==p:
    print('number is spy number')
else:
    print('number is not spy number ')