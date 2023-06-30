# pip install multipledispatch
#in backend, dispatcher crwates an object which stores different implementation and on runtime, it selects the appropriate methoad as the type and number of parameters passed

from multipledispatch import dispatch
@dispatch(int, int)
def product(first, second):
    result = first*second
    print(result);


@dispatch(int, int, int)
def product(first, second, third):
    result = first * second *third
    print(result);

@dispatch(float, float, float)
def product(first, second, third):
    result = first * second *third
    print(result);
