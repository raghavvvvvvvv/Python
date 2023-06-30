#ex: 153 3 cube 27 5^3 125 1^1 ---> 153, home work perfect number, spy number
n=int(input('enter number '))
s=0
temp=n
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
if temp==s:
    print('number is pallindrome ')
else:
    print('number is not pallindrome ')