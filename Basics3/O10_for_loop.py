"""
for loops = Execute a block of code a fixed number of times.
            You can iterate  it over a range,string,sequence,etc.
"""
'''
| Loop Type        | When to Use                                                                            | How It Works                                                     |
| ---------------- | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **`for` loop**   | When you know **how many times** you want to repeat an action (fixed iteration).       | Iterates over a **sequence** (like a list, range, string, etc.). |
| **`while` loop** | When you **don’t know** how many times you’ll need to repeat (conditional repetition). | Repeats **as long as a condition is true**.                      |
'''

# Demonstration of for loop iteration over range
# range(start, stop, step)

for counter in range(1,101):
    print(counter)

# for p in reversed(range(1,101)):
#     print(p)

#Print reverse order of number 
for x in reversed(range(1,11)):
    print(x)
print("Happy New Year!")

#To print odd numbers between 
for u in range(1,101,2):
    print(u)
for v in range(2,101,2):
    print(v)