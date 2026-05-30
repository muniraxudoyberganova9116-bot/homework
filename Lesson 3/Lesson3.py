# List Tasks

# 1. Count Occurrences: Given a list and an element, find how many times the element appears in the list.
print("Task 1: Count Occurrences")
numbers = [1, 2, 3, 4, 2, 5, 2]
element = 2
count = numbers.count(element)
print(f"The element {element} appears {count} times in the list.")

# 2. Sum of Elements: Given a list of numbers, calculate the total of all the elements.
print("\nTask 2: Sum of Elements")
total_sum = sum(numbers)
print(f"The sum of the elements in the list is: {total_sum}")

# 3. Max Element: From a given list, determine the largest element.
print("\nTask 3: Max Element")
max_element = max(numbers)
print(f"The largest element in the list is: {max_element}") 

# 4. Min Element: From a given list, determine the smallest element.
print("\nTask 4: Min Element")
min_element = min(numbers)
print(f"The smallest element in the list is: {min_element}")

# 5. Check Element: Given a list and an element, check if the element is present in the list.
print("\nTask 5: Check Element")
element = 3 
if element in numbers:
    print(f"The element {element} is present  in the list.")

# 6. First Element: Access the first element of a list, considering what to return if the list is empty.
print("\nTask 6: First Element")
nums = []  # Example of an empty list
if nums:  # Check if the list is not empty
    first_element = nums[0]
    print(f"The first element of the list is: {first_element}")
else:
    print("The list is empty, no first element to access.")

# 7. Last Element: Access the last element of a list, considering what to return if the list is empty.
print("\nTask 7: Last Element")
if nums:  # Check if the list is not empty
    last_element = nums[-1]
    print(f"The last element of the list is: {last_element}")
else:
    print("The list is empty, no last element to access.")

# 8. Slice List: Create a new list that contains only the first three elements of the original list.
print("\nTask 8: Slice List")
original_list = [70, 80, 10, 20, 30, 40, 50]
sliced_list = original_list[:3]
print(f"The new list containing the first three elements is: {sliced_list}")

# 9. Reverse List: Create a new list that contains the elements of the original list in reverse order.
print("\nTask 9: Reverse List")
reversed_list = original_list[::-1]
print(f"The reversed list is: {reversed_list}")

# 10. Sort List: Create a new list that contains the elements of the original list in sorted order.
print("\nTask 10: Sort List")
sorted_list = sorted(original_list)
print(f"The sorted list is: {sorted_list}")

# 11. Remove Duplicates: Given a list, create a new list that contains only unique elements from the original list.
print("\nTask 11: Remove Duplicates")
list_with_duplicates = [1, 2, 3, 2, 4, 5, 1]
unique_list = list(set(list_with_duplicates))
print(f"The list with duplicates removed is: {unique_list}")

# 12. Insert Element: Given a list and an element, insert the element at a specified index.
print("\nTask 12: Insert Element")
my_list = [1, 2, 3, 4, 5]
element_to_insert = 10
index_to_insert = 2
my_list.insert(index_to_insert, element_to_insert)
print(f"The list after inserting {element_to_insert} at index {index_to_insert} is: {my_list}") 

# 13. Index of Element: Given a list and an element, find the index of the first occurrence of the element.
print("\nTask 13: Index of Element")
element_to_find = 3
if element_to_find in my_list:
    index = my_list.index(element_to_find)
    print(f"The index of the first occurrence of {element_to_find} is: {index}")    

# 14. Check for Empty List: Determine if a list is empty and return a boolean.
print("\nTask 14: Check for Empty List")
empty_list = []
is_empty = len(empty_list) == 0
print(f"Is the list empty? {is_empty}")     
# 15. Count Even Numbers: Given a list of integers, count how many of them are even.
print("\nTask 15: Count Even Numbers")
even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
print(f"The number of even numbers in the list is: {even_count}")

# 16. Count Odd Numbers: Given a list of integers, count how many of them are odd.
print("\nTask 16: Count Odd Numbers")
odd_count = 0
for num in numbers:
    if num % 2 != 0:
        odd_count += 1
print(f"The number of odd numbers in the list is: {odd_count}")

# 17. Concatenate Lists: Given two lists, create a new list that combines both lists.
print("\nTask 17: Concatenate Lists")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(f"The concatenated list is: {concatenated_list}")

# 18. Find Sublist: Given a list and a sublist, check if the sublist exists within the list.
print("\nTask 18: Find Sublist")
main_list = [1, 2, 3, 4, 5]
sublist = [2, 3]
if all(item in main_list for item in sublist):
    print(f"The sublist {sublist} exists within the main list.")

# 19. Replace Element: Given a list, replace the first occurrence of a specified element with another element.
print("\nTask 19: Replace Element")
my_list = [1, 2, 3, 4, 5]
element_to_replace = 3
new_element = 10
if element_to_replace in my_list:
    a = my_list.index(element_to_replace)
    my_list[a] = 10
print("the updated list is : ", my_list)

# 20. Find Second Largest: From a given list, find the second largest element.
print("\nTask 20, Find second max")
new_list = [1, 2, 2, 4, 89, 10, 35]
new_list.remove(max(new_list))
print(max(new_list))

# 21. Find Second Smallest: From a given list, find the second smallest element.
print("\nTask 21. Find second smallest")
new_list.remove(min(new_list))
print(min(new_list))

# 22. Filter Even Numbers: Given a list of integers, create a new list that contains only the even numbers.
print("\nTask22")
integers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for num in integers:
    if num % 2 == 0:
        evens.append(num)
print(evens)
    

# 23. Filter Odd Numbers: Given a list of integers, create a new list that contains only the odd numbers.
print("\nTask 23")
odds = []
for num in integers:
    if num % 2 != 0:
        odds.append(num)
print(odds)

# 24. List Length: Determine the number of elements in the list.
print("\nTask 24:")
print(len(integers))

# 25. Create a Copy: Create a new list that is a copy of the original list.
print("\n task 25: ")
print(integers.copy())

# 26. Get Middle Element: Given a list, find the middle element. If the list has an even number of elements, return the two middle elements.
print("\n task 26: ")
a = int(len(integers)/2)
if len(integers)%2 != 0 :
    print(integer[a], " is the middle element")
else: 
    print(integers[a-1], "and", integers[a] , "are middle elements")

# 27. Find Maximum of Sublist: Given a list, find the maximum element of a specified sublist.
print("\n Task 27")
main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sublist = main_list[2:6] 
max_sublist = max(sublist)
print(f"The maximum element of the sublist {sublist} is: {max_sublist}")    

# 28. Find Minimum of Sublist: Given a list, find the minimum element of a specified sublist.
print("\n Task 28")
min_sublist = min(sublist)
print(f"The minimum of sublist {sublist} is: {min_sublist} ")

# 29. Remove Element by Index: Given a list and an index, remove the element at that index if it exists.
print("\n Task 29")
ind = 4
main_list.pop(ind)
print(main_list)

# 30. Check if List is Sorted: Determine if the list is sorted in ascending order and return a boolean.
print("\nTask 30")
if main_list == sorted(main_list):
    print(f"The main list {main_list} is sorted ")
else:
    print(f"{main_list} not sorted")


# 31. Repeat Elements: Given a list and a number, create a new list where each element is repeated that number of times.
print("\n Task 31")

myList = [1, 2, 3]
frequency = 2
repeated_list = []
for element in myList:
    repeated_list.extend([element] * frequency)
print(f"The new list with each element repeated {frequency} times is: {repeated_list}")

# 32. Merge and Sort: Given two lists, create a new sorted list that merges both lists.
print("\n Task 32")
list1 = [1, 12, 3]
list2 = [14, 5, 3]
merged_list = sorted(list1 + list2)
print(f"{merged_list} is the sorted and merged one")

# 33. Find All Indices: Given a list and an element, find all the indices of that element in the list.
print("\n Task 33")
element = 3
print(f"{element} appears at indexes:")
for index, num in enumerate(merged_list):
    if num == element:
        print(index)

# 34. Rotate List: Given a list, create a new list that is a rotated version of the original list (shift elements to the right).
print("\nTask 34")
newlist = merged_list[::-1]
print(f"{merged_list} is reversed and here is the result: {newlist}")

# 35. Create Range List: Create a list of numbers in a specified range (e.g., from 1 to 10).
print("\nTask35")
mylist=[]
for i in range(10):
    mylist.append(i+1)
print(mylist)

# 36. Sum of Positive Numbers: Given a list of numbers, calculate the sum of all positive numbers.
print("\nTask36")
mylist = [-1, 3, -4, 5, -90, 78]
total = 0
for num in mylist:
    if num > 0:
        total += num
print(f"for {mylist}, {total} is the sum of positive numbers")
# 37. Sum of Negative Numbers: Given a list of numbers, calculate the sum of all negative numbers.
print("\nTask37")
total = 0
for num in mylist:
    if num < 0:
        total += num
print(f"for {mylist}, {total} is the sum of negative numbers")


# 38. Check Palindrome: Given a list, check if the list is a palindrome (reads the same forwards and backwards).
print("\nTask38")
mylist = [-1, 3, -4, 3, -1 ]

if mylist == mylist[::-1]:
    print("palindrome ")
else: 
    print("not palindrome")
# 39. Create Nested List: Create a new list that contains sublists, where each sublist contains a specified number of elements from the original list.
print("\nTask39")
original = [1, 2, 3, 4, 5, 6, 9, 8, 1, 5, 7, 8 , 9 ]
newlist = [ original[:2], 
            original[2:5], 
            original[5:]
            ]
print(newlist)
# 40. Get Unique Elements in Order: Given a list, create a new list that contains unique elements while maintaining the original order.
print("\nTask40")
print(sorted(set(original)))

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

# ### Set Tasks

# 1. **Union of Sets**: Given two sets, create a new set that contains all unique elements from both sets.
print("\ntask1")
myset1 = {1, 2, 3, 4}
myset2 = {3, 4, 5, 6}
union_set = myset1.union(myset2)
print("Union of sets: ", union_set)

# 2. **Intersection of Sets**: Given two sets, create a new set that contains elements common to both sets.
print("\ntask2")
intersection_set = myset1.intersection(myset2)
print("intersected set is ", intersection_set)

# 3. **Difference of Sets**: Given two sets, create a new set with elements from the first set that are not in the second.
print("\ntask3")
difference = myset1.difference(myset2)
print("the difference is ", difference)

# 4. **Check Subset**: Given two sets, check if one set is a subset of the other.
print("\ntask4")
original = {1, 2, 3, 4, 5}
subset = {2, 3, 8}
if subset.issubset(original):
    print("it is subset")
else: 
    print("not subset")
   
# 5. **Check Element**: Given a set and an element, check if the element exists in the set.
print("\ntask5")
element = 4
if element in subset:
    print("exists")
else:
    print("not present")

# 6. **Set Length**: Determine the number of unique elements in a set.
print("\ntask6")
unique = 0
set1 = { 1, 2, 2, 3, 3, 4, 5}
set2 = set(set1)
print(set2, " has ", len(set2), "elements")
# 7. **Convert List to Set**: Given a list, create a new set that contains only the unique elements from that list.
print("\ntask7")
mylist = [1, 2, 6 , 1, 2, 7 ,3 , 4,5 ]
myset = set(mylist)
print("set is ", myset)

# 8. **Remove Element**: Given a set and an element, remove the element if it exists.
print("\ntask8")
element = 9
if element in myset:
    myset.remove(element)
    print(myset)
else:
    print("the element is not present in the set")
# 9. **Clear Set**: Create a new empty set from an existing set.
print("\ntask9")
myset.clear()
print("the set is cleared ", myset)
# 10. **Check if Set is Empty**: Determine if a set has any elements.
print("\ntask10")
myset = {1, 2, 4}
if len(myset) == 0:
    print("the set is empty")
else:
    print("the set is not empty")
# 11. **Symmetric Difference**: Given two sets, create a new set that contains elements that are in either set but not in both.
print("\ntask11")
symmetric_difference = myset1.symmetric_difference(myset2)
print("the symmetric difference is", symmetric_difference)

# 12. **Add Element**: Given a set and an element, add the element to the set if it is not already present.
print("\ntask12")
element = 10
if element in set1:
    print("it already exists")
else:
    set1.add(element)
    print("the element", element,"added to the set ", set1)

# 13. **Pop Element**: Given a set, remove and return an arbitrary element from the set.
print("\ntask13")
set1.remove(1)
print("removed 1", set1)
set1.add(1)
print("returned 1", set1)

# 14. **Find Maximum**: From a given set of numbers, find the maximum element.
print("\ntask14")
print(max(set1), "is the maximum in", set1)

# 15. **Find Minimum**: From a given set of numbers, find the minimum element.
print("\n ")
print(min(set1), "is the minimum in", set1 )

# 16. **Filter Even Numbers**: Given a set of integers, create a new set that contains only the even numbers.
print("\ntask16")
newset=set(num for num in set1 if num%2 == 0) 
print(newset, "is the new set created from ", set1)

# 17. **Filter Odd Numbers**: Given a set of integers, create a new set that contains only the odd numbers.
print("\ntask17")
newset=set(num for num in set1 if num%2 == 1) 
print(newset, "is the new set created from ", set1)
# 18. **Create a Set of a Range**: Create a set of numbers in a specified range (e.g., from 1 to 10).
print("\ntask18")
rangeset = set( i+1 for i in range(10))
print(rangeset)
# 19. **Merge and Deduplicate**: Given two lists, create a new set that merges both lists and removes duplicates.
print("\ntask19")
set3 =  set1.union(set2)
print(set1, "and", set2, "are merged into ",set3)

# 20. **Check Disjoint Sets**: Given two sets, check if they have no elements in common.
print("\ntask20")
if len(set1.intersection(set2)) != 0:
    print("it has common elements ", set1.intersection(set2))
else:
    print("no common elements")

# 21. **Remove Duplicates from a List**: Given a list, create a set from it to remove duplicates, then convert back to a list.
print("\ntask21")
print(mylist)
mylist = list(set(mylist))
print(mylist, "duplicates removed")
# 22. **Count Unique Elements**: Given a list, determine the count of unique elements using a set.print
print("\ntask22")
list1 = [1, 2, 6, 1, 2, 7, 3, 4, 5]
print(set(list1), "are unique elements")

# 23. **Generate Random Set**: Create a set with a specified number of random integers within a certain range.
print("\ntask23")
import random
random_set = set(random.randint(1, 100) for _ in range(10))
print("random set is ", random_set) 



# ### Dictionary Tasks

# 1. **Get Value**: Given a dictionary and a key, retrieve the associated value, considering what to return if the key doesn’t exist.
print("\ntask1")
mydict = {"name": "Alice", "age": 30, "city": "New York"}
key = "name"
if key in mydict:
    value = mydict[key]
    print(f"The value for key '{key}' is: {value}")
else:
    print(f"Key '{key}' does not exist in the dictionary.") 

# 2. **Check Key**: Given a dictionary and a key, check if the key is present in the dictionary.
print("\ntask2")
key2 = "country"
if key2 in mydict:
    print(f"Key '{key2}' exists in the dictionary.")
else:
    print(f"Key '{key2}' does not exist in the dictionary.")

# 3. **Count Keys**: Determine the number of keys in the dictionary.
print("\ntask3")
print("there are ", len(mydict), "keys in the dictionary")

# 4. **Get All Keys**: Create a list that contains all the keys in the dictionary.
print("\ntask4")
mylist = list(key for key in mydict)
print("here are the keys: ", mylist)

# 5. **Get All Values**: Create a list that contains all the values in the dictionary.
print("\ntask5")
values = list(mydict[key] for key in mydict)
print("here are the values", values)

# 6. **Merge Dictionaries**: Given two dictionaries, create a new dictionary that combines both.
print("\ntask6")
dict1 = {"name": "Alice", "age": 30}
dict2 = {"city": "New York", "country": "USA"}
dict3 = dict1 | dict2
print(dict3)

# 7. **Remove Key**: Given a dictionary and a key, remove the key if it exists, handling the case if it doesn’t.
print("\ntask7")
if key in mydict:
    mydict.pop(key)
    print(mydict)
else:
    print("the key deosnt exist")

# 8. **Clear Dictionary**: Create a new empty dictionary.
print("\ntask8")
print("Cleared: ", mydict.clear(), type(mydict))

# 9. **Check if Dictionary is Empty**: Determine if a dictionary has any elements.
print("\ntask9")
if len(mydict) == 0:
    print("the dictionary is empty")
else:
    print("the dictionary is not empty")
# 10. **Get Key-Value Pair**: Given a dictionary and a key, retrieve the key-value pair if the key exists.
print("\ntask10")
mydict = {"name": "Alice", "age": 30, "city": " Alice", "lastname": "Alice"}
if key in mydict:
    print(key, ":", mydict[key])
else:
    print(mydict, "is empty")
# 11. **Update Value**: Given a dictionary, update the value for a specified key.
print("\ntask11")
mydict[key] = "hello"
print(key,":", mydict[key])

# 12. **Count Value Occurrences**: Given a dictionary, count how many times a specific value appears across the keys.
print("\ntask12")
mydict = {"name": "Alice",  "city": "Alice", "lastname": "Alice",}
value = "Alice"
total = 0
for i in mydict:
    if mydict[i] == value:
        print(mydict[i])
        total = total +1
    else: 
        print("such element doesnt exist")
print(total, "times", value, " appeared in ", mydict)

# 13. **Invert Dictionary**: Given a dictionary, create a new dictionary that swaps keys and values.
print("\ntask13")
inverted_dict = {value: key for key, value in mydict.items()}
print("the inverted dictionary is ", inverted_dict)

# 14. **Find Keys with Value**: Given a dictionary and a value, create a list of all keys that have that value.
print("\ntask14")
mydict = {"name": "Alice",  "city": " Alice", "lastname": "Alice",}
value = "Alice"
keys_with_value = [key for key, val in mydict.items() if val == value]
print(f"Keys with value '{value}': {keys_with_value}")      

# 15. **Create a Dictionary from Lists**: Given two lists (one of keys and one of values), create a dictionary that pairs them.
print("\ntask15")
keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]
new_dict = dict(zip(keys, values))
print("the new dictionary is ", new_dict)

# 16. **Check for Nested Dictionaries**: Given a dictionary, check if any values are also dictionaries.
print("\ntask16")
mydict = {"name": "Alice", "age": 30, "address": {"city": "New York", "zip": "10001"}}
for key, value in mydict.items():
    if type(value) == dict:
        print(f"The value for key '{key}' is a nested dictionary: {value}") 
    
# 17. **Get Nested Value**: Given a nested dictionary, retrieve a value from within one of the inner dictionaries.
print("\ntask17")
nested_dict = {"name": "Alice", "age": 30, "address": {"city": "New York", "zip": "10001"}}
city = nested_dict["address"]["city"]
print("the city is ", city) 

# 18. **Create Default Dictionary**: Create a dictionary that provides a default value for missing keys.
print("\ntask18")
from collections import defaultdict
default_dict = defaultdict(lambda: "default value")
default_dict["existing_key"] = "existing value"
print("existing_key:", default_dict["existing_key"])  # Output: existing value
print("missing_key:", default_dict["missing_key"])    # Output: default value

# 19. **Count Unique Values**: Given a dictionary, determine the number of unique values it contains.
print("\ntask19")
mydict = {"name": "Alice", "age": 30, "city": "New York", "lastname": "Alice"}
unique_values = set(mydict.values())
print("Unique values:", unique_values)
print("Number of unique values:", len(unique_values))

# 20. **Sort Dictionary by Key**: Create a new dictionary sorted by keys.
print("\ntask20")
sorted_dict_by_key = dict(sorted(mydict.items()))
print("Dictionary sorted by keys:", sorted_dict_by_key)

# 21. **Sort Dictionary by Value**: Create a new dictionary sorted by values.
# print("\ntask21")
# sorted_dict_by_value = dict(sorted(mydict.items(), key=lambda item: item[1]))
# print("Dictionary sorted by values:", sorted_dict_by_value)
# #have no ideas

# 22. **Filter by Value**: Given a dictionary, create a new dictionary that only includes items with values that meet a certain condition.
print("\ntask22")
filtered_dict = {key: value for key, value in mydict.items() if isinstance(value, str) and value.startswith("A")}
print("Filtered dictionary (values starting with 'A'):", filtered_dict)

# 23. **Check for Common Keys**: Given two dictionaries, check if they have any keys in common.
print("\ntask23")
dict1 = {"name": "Alice", "age": 30}
dict2 = {"name": "Bob", "city": "New York"}
common_keys = set(dict1.keys()) & set(dict2.keys())
if common_keys:
    print("Common keys:", common_keys)
else:    print("No common keys")    

# 24. **Create Dictionary from Tuple**: Given a tuple of key-value pairs, create a dictionary from it.
print("\ntask24")
tuple_of_pairs = (("name",  "Alice"), ("age", 30), ("city", "New York"))
new_dict = dict(tuple_of_pairs)
print("the new dictionary is ", new_dict)

# 25. **Get the First Key-Value Pair**: Retrieve the first key-value pair from a dictionary.
print("\ntask25")
first_key_value_pair = next(iter(mydict.items()))
print("the first key-value pair is ", first_key_value_pair)