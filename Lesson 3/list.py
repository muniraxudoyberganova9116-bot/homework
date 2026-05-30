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
