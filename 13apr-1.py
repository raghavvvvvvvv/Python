class x:
    def m1(self,a=0,b=0,c=0):
        if a == 0 and  b == 0 and c == 0:
            print('Method is called with no argument')
        elif a!=0 and b!=0 and c == 0:
            self.a=a
            print(self.a)
            print('Method is called with single argument')
        else:
            self.a=a
            self.b=b
            self.c=c
            print(self.a)
            print('Method is called with three argument')
xobj = x()
xobj.m1()
xobj.m1(10)
xobj.m1(20,30)
xobj.m1(40,50,60)

