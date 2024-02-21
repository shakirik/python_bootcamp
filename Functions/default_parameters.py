# setting a default parameter but when you set your own, it overrides the default set

def exponent (num, power=2):
    return num ** power

print(exponent(1))
print(exponent())
print(exponent(53))

# default parameter can be anything, doesn't have to be a string, can be boolean etc
# have to make sure defaults go to the end as python does everything in order


def add(a, b):
    return a+b

def math(a, b, fn=add):
    return fn (a, b)

def subtract (a, b):
    return a - b

print(math(2, 3, subtract))