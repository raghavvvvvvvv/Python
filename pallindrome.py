# reverse will be same
n=int(input('enter number '))
s=0
temp=n
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
if temp==s:
    print('number is palindrome ')
else:
    print('number is not palindrome ')