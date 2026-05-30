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
#have no ideas

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