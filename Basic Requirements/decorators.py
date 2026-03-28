# illustration 1
def div(a,b):
    print(a/b)

# Now we want ot change the div function without changing its definition
# What we want to do is make smart_div which always make larger number a numerator

def smart_div(func):
    # make inner function which takes func as argument
    def inner(x,y):
        if x<y:
            x,y = y,x
        return func(x,y)
    return inner

new_div = smart_div(div)
new_div(2,8)

div = smart_div(div)
div(2,4)

# illustration 2
import time 

def counter(fx):
    def mfx(*args, **kwargs):
        start = time.perf_counter()
        print("Starting the execution")
        fx(*args, **kwargs)
        end = time.perf_counter()
        print("Execution complete, Elapsed time:", end - start)
    return mfx

@counter
def hello():
    print("Hello world!!")

@counter
def make_and_sort():
    my_list = [i for i in range(99999999,1,-1)]
    my_list.sort()

# make_and_sort()
hello()

#illustration 3
def add_5(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)+5
    return wrapper

def add_10(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)+10
    return wrapper

@add_5 
@add_10
def add(a,b):
    return a+b

print(add(1,2)) #18


# question i found
def double(func):  
    def wrapper():  
        func()  
        func()  
        func()
    return wrapper    
@double
def f1():  
    print("Hello There")  
f1()  