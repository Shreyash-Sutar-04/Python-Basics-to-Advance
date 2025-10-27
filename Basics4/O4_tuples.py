# Tuples --> Ordered unchangable duplicates allowed and faster compare to lists sets
# Represented by ()
import time
colours = ("green","red","orange","purple","gray","indigo","pink")
print(colours) 
print(len(colours))
print("pineapple" in colours)
indeex = colours.index("green")
print(indeex)
print(colours.count("purple"))

for colour in colours:
    time.sleep(1)
    print(f"{colour}")

#Always prefer tuples over a list

