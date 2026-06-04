print("Task 1")

convert_cel_to_far = lambda C: round(C * 9/5 + 32, 2)
convert_far_to_cel = lambda F: round((F - 32) * 5/9, 2) 

far = int(input("Enter a temperature in degrees F: "))
print(far, "degrees F =", convert_far_to_cel(far), "degrees C")

cel = int(input("Enter a temperature in degrees C: "))
print(cel, "degrees C =", convert_cel_to_far(cel), "degrees F")


print("\nTask 2")

def invest(deposit, rate, years):
    for i in range(1, years + 1):
        print("year", i, ": $", round(deposit * (1 + rate/100) ** i, 2))
d, r, y = int(input("enter the deposit: ")), int(input("enter the interest rate: ")), int(input("enter the number of years: "))
invest(d, r, y)

print("\nTask 3")

integer = int(input("enter an integer: "))
for i in range(1, integer + 1):
    if integer % i == 0:
        print(i, "is a factor of", integer)

print("\nTask 4")

print("\nTask 4")

students = []
tuition = []

def enrollment_stats(uni):
    for val in uni:
        students.append(val[1])
        tuition.append(val[2])

def mean( l ):
    mean = round(sum(l) / len(l), 2)
    return mean

def median( l ):
    if len(l)%2 == 0:
        middle = len(l)/2
        median = ( l[middle] + l [middle -1])/2
    else:
        middle = len(l)//2
        median = l[middle]
    return median

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
enrollment_stats(universities)
print("Total students:", sum(students))
print("Total tuition: $", sum(tuition), "\n")

print("Student mean: ", mean(students))
print("Student median: ", median(sorted(students)), "\n")

print("Tuition mean: $", mean(tuition))
print("Tuition median: $", median(sorted(tuition)), "\n")



print("\nTask 5")
# Define a function `is_prime(n)` which returns `True` if the given $n$ ($n$ > 0) is _prime number_, otherwise returns `False`
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True 

print(is_prime(19))
