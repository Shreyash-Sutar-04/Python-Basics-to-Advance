import random 
# Module that gives a lot of random methods for number and other stuff

# A dice have 1 to 6 numbers so to generate the numbers randomly 
dice_number = random.randint(1,6)
print(dice_number)

# If you want the floating point number then you have to use the "random" method
number = random.random()
print(number)

# Rock Paper Scissor logic
option = ["Rock","Paper","Scissor"]
print(random.choice(option))

# Deck Cards shuffle logic idea
deck = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
random.shuffle(deck)
print(deck)







