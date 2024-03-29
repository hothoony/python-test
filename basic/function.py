
def my_func1():
    print('my_func1 called')

def my_func2():
    print('my_func2 called')
    my_func1()
    my_func1()
    my_func1()

my_func2()

def sum(a, b):
    return a + b

result = sum(10, 20)
print(result)

def my_func_default_parameter(name = 'paul'):
    print(name)

my_func_default_parameter()
my_func_default_parameter('judy')
