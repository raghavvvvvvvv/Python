def computeday(h,r):
    if h>40:
        p=1.5*r*(h-40)+(40*r)
    else:
        p=h*r
    return p
hrs=input("Enter hrs:")
hr=float(hrs)
rhrs=input("Enter rate per hour: ")
rphrs=float(rhrs)
p=computeday(hr,rphrs)
print(p)