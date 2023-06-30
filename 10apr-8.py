x = 1
def func():
    x=20
    print(x)
    def func1():
        x = 10
        print(x)
    func1()
func()
print(x)