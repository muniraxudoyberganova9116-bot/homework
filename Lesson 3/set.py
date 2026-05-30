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
