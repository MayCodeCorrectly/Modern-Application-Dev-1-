def decor(func):
    def wrapper(x):
        y = func(x)
        return y*x
    return wrapper

@decor
def inner(x,optional= "Hello world"):
    return x,optional

print(inner(5))