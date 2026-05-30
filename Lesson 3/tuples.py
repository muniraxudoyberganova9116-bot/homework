# Tuple Tasks

# 1. Count Occurrences: Given a tuple and an element, find how many times the element appears in the tuple.
print("Task1")
tuple1 = (1, 2, 3, 4, 2, 5, 2)
element = 2
occurrences = tuple1.count(element)
print(f"The element {element} appears {occurrences} times in the tuple {tuple1}.")

# 2. Max Element: From a given tuple, determine the largest element.
print("\nTask2")
print(max(tuple1), " is the maximum")

# 3.  Min Element: From a given tuple, determine the smallest element.
print("\nTask2")
print(min(tuple1), " is the minimum")

# 4.  Check Element: Given a tuple and an element, check if the element is present in the tuple.
print("\nTask4")
if element in tuple1:
    print(f"{element} exists in the tuple {tuple1}")
else:
    print(f" {element} is not present in the tuple {tuple1}")

# 5.  First Element: Access the first element of a tuple, considering what to return if the tuple is empty.
print("\nTask 5")
tuple2=(2, 3, 5, 7)
if len(tuple2) != 0:
    print("the first element of tuple", tuple2, " is ", tuple2[0])
else: 
    print("empty tuple")
# 6.  Last Element: Access the last element of a tuple, considering what to return if the tuple is empty.
print("\ntask6")
if len(tuple2) != 0:
    print("the last element of tuple", tuple2, " is ", tuple2[-1])
else: 
    print("empty tuple")
# 7.  Tuple Length: Determine the number of elements in the tuple.
print("\nTask7")
print("the number of elements in ", tuple2, " is: ", len(tuple2))

# 8.     Slice Tuple: Create a new tuple that contains only the first three elements of the original tuple.
print("\nTask8")
newtuple = tuple2[:3]
print("the new tuple is ", newtuple)

# 9.     Concatenate Tuples: Given two tuples, create a new tuple that combines both.
print("\ntask9")
tuple3 = (1, 2, 3)
tuple4 = (3, 6, 7)
tuple5 = tuple3 + tuple4
print("the combined tuple is ", tuple5)

# 10.    Check if Tuple is Empty: Determine if a tuple has any elements.
print("\nTask10")
if len(tuple4)==0:
    print("the tuple ", tuple4 ,"is empty")
else:
    print("the tuple is ", tuple4)
# 11.    Get All Indices of Element: Given a tuple and an element, find all the indices of that element in the tuple.
print("\nTask 11")
tuple6 = (1, 2, 3, 3, 4, 3, 8)
element2 = 3
indices = [index for index, value in enumerate(tuple6) if value == element2]
print(f"The indices of element {element2} in the tuple are: {indices}")

# 12.    Find Second Largest: From a given tuple, find the second largest element.
print("\nTask12")
unique_elements = set(tuple1)
if len(unique_elements) < 2:
    print("There is no second largest element.")
else:
    sorted_elements = sorted(unique_elements, reverse=True)
    second_largest = sorted_elements[1]
    print(f"The second largest element in the tuple {tuple1} is: {second_largest}")

# 13.    Find Second Smallest: From a given tuple, find the second smallest element.
print("\nTask13")
if len(unique_elements) < 2:
    print("There is no second smallest element.")
else:
    sorted_elements = sorted(unique_elements)
    second_smallest = sorted_elements[1]
    print(f"the second smallest is  {second_smallest}")

# 14.    Create a Single Element Tuple: Create a tuple that contains a single specified element.
print("\ntask14")
tuple7 = (9,)
print("here is the tuple : ", tuple7, type(tuple7))

# 15.    Convert List to Tuple: Given a list, create a tuple containing the same elements.
print("\ntask15")
list1 = [ "hello", 8, 9.8 ]
tuple8 = tuple(list1)
print(tuple8, type(tuple8))

# 16.    Check if Tuple is Sorted: Determine if the tuple is sorted in ascending order and return a boolean.
print("\ntask16")
print( tuple7 == sorted(tuple6))

# 17.    Find Maximum of Subtuple: Given a tuple, find the maximum element of a specified subtuple.
print("\ntask17")
subtuple6 = tuple6[ 2:7]
print(max(subtuple6), "is the maximum of ", subtuple6)

# 18.    Find Minimum of Subtuple: Given a tuple, find the minimum element of a specified subtuple.
print("\ntask18")
print(min(subtuple6), "is the minimum of ", subtuple6)

# 19.    Remove Element by Value: Given a tuple and an element, create a new tuple that removes the first occurrence of that element.
print("\ntask19")
for i, v in enumerate(tuple6):
    if v == element2:
        new_tuple = tuple6[:i] + tuple6[i+1:]
        break    
print("the new tuple is ", new_tuple)   

# 20.    Create Nested Tuple: Create a new tuple that contains subtuples, where each subtuple contains specified elements from the original tuple.
print("\ntask20")
tuple9 = (1, 2, 3, 4, 5, 6)
nested_tuple = tuple((tuple9[i:i+2]) for i in range(0, len(tuple9), 2))
print("the nested tuple is ", nested_tuple) 

# 21.    Repeat Elements: Given a tuple and a number, create a new tuple where each element is repeated that number of times.
print("\ntask21")
tuple10 = sorted(tuple9 * element2)
print("the new tuple is repeated ", element2, " times ", tuple10) 
# 22.    Create Range Tuple: Create a tuple of numbers in a specified range (e.g., from 1 to 10).
print("\ntask22")
numbers = tuple(i+1 for i in range(10))
print("here is the range tuple ", numbers)
# 23.    Reverse Tuple: Create a new tuple that contains the elements of the original tuple in reverse order.
print("\ntask23")
newtuple = tuple(reversed(numbers))
print("here is the reversed version", newtuple)

# 24.    Check Palindrome: Given a tuple, check if the tuple is a palindrome (reads the same forwards and backwards).
print("\ntask24")
tuple10 = ( 2, 3, 4, 5, 4, 3, 2, 1)
if tuple10 == tuple(reversed(tuple10)):
    print("the palindrome is correct")
else:
    print("not palindrome")

# 25.    Get Unique Elements: Given a tuple, create a new tuple that contains only the unique elements while maintaining the original order.
print("\ntask25")
tuple11 = set(tuple10)
print("here is the unique elements", tuple11)