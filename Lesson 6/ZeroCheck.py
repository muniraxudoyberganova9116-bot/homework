# ### Zero Check Decorator

# Write a decorator function called `check` 
# that verifies that the denominator is not equal to 0 and apply it to the following function:

# python
# @check
# def div(a, b):
#    return a / b

# input: div(6, 2)
# output: 3

# input: div(6, 0)
# output: "Denominator can't be zero"

def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        else:
            return func(a, b)
    return wrapper

@check
def div(a, b):
    return a / b    

print(div(6, 2))
print(div(6, 0))