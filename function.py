def fact(x):
    if x==0:
        return 1;
    else:
        return x*fact(x-1)
n=int(input('Enter a number'))
print('Factorial of a {} is {}'.format(n,fact(n)))