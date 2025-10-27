capitals = {"USA" : "Washington DC",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow",
            "Brazil":"Brasilia",
            "France":"Paris"} 

"""
student = {"name": "Shreyash", "age": 21, "course": "Python"} 
print(student.items()) 
print(student) 
by comparing how these outputs differs
| Expression        | Data Type                  | Appearance                                                              | Purpose                             |
| ----------------- | -------------------------- | ----------------------------------------------------------------------- | ----------------------------------- |
| `student`         | `dict`                     | `{'name': 'Shreyash', 'age': 21, 'course': 'Python'}`                   | Shows the actual dictionary         |
| `student.items()` | `dict_items` (view object) | `dict_items([('name', 'Shreyash'), ('age', 21), ('course', 'Python')])` | Shows pairs as tuples (for looping) |

Items basically resembles a 2D list of tuples
"""

Items = capitals.items()
print(Items)

'''
.items() returns a view object — a special iterable called dict_items.
Inside that, you have a list of tuples,
and each tuple represents one key–value pair.
'''
#Now if you want to print a clean key-value pair of a dictionary without braces,commas

for item in capitals.items():
    print(item)
# The above method will simply print the key value combination treating it as a tuple

for key,value in capitals.items():
    print(key,value)
    print(f"{key}:{value}")

# for key in capitals.keys():
#     for value in capitals.values():
#         print(f"{key}:{value}")
#This will show why the upper method to print the key value is more convenient















