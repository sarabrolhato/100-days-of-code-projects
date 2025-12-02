### Day 26 - List Comprehension and the NATO Alphabet
- Day 26 Project: the NATO Alphabet Project

#### List Comprehension

We can use list comprehensions to create a new list from a previous list. For example, if we want to create a new list where every number in the original list is increased by 1, we could do it using a for loop:

```
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n+1
    new_list.append(add_1)
```
Using a list comprehension, this could be written with a single line of code:
```
new_list = [n + 1 for n in numbers]
```

A general way of expressing a list comprehension is:
```
new_list = [new_item for item in list]
```

#### Conditional List Comprehension
```
new_list = [new_item for item in list if test]
```

#### Dictionary Comprehension

Creating a dictionary using this shortened syntax:
```
new_dict = {new_key:new_value for item in list}
```

Creating a new dictionary based on the values of an existing dictionary:
```
new_dict = {new_key:new_value for (key,value) in dict.items()}
```

#### Conditional Dictionary Comprehension
```
new_dict = {new_key:new_value for (key,value) in dict.items() if test}
```

#### How to Iterate over a Pandas Dataframe

Looping through the column names of a dataframe:
```
for (key, value) in student_data_frame.items():
    print(key)
```

Looping through the values of every column:
```
for (key, value) in student_data_frame.items():
    print(value)
```

Looping through each row of the dataframe:
```
for (index, row) in student_data_frame.iterrows():
    print(row)
```

Looping through each row of a specific column:
```
for (index, row) in student_data_frame.iterrows():
    print(row.student)
```