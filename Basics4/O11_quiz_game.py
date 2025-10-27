#Python Quiz game

questions = ("How many elements are in there periodic table? :",
             "Which animal lays the largest eggs? :",
             "What is the most abundent gas in earths atmosphere? :",
             "How many bones are in human body? :",
             "Which planet in solar system is the hottest?") # A tuple consist questions
options = (("A.116 ","B. 118 ","C. 117 ","D. 119 "),
           ("A.Whale ","B.Crocodile ","C.Elephant ","D.Ostrich"),
           ("A.Nitrogen","B.Oxygen","C.Carbon-Dioxide","D.Hydrogen"),
           ("A.206","B.207","C.208","D.209"),
           ("A.Mercury","B.Venus","C.Earth","D.Mars")) #2D tuple for options for each question
answers = ("C","D","A","A","B") #Tuple for answers
guesses = [] #We are appending the user input into guesses so thats why list
score = 0
question_num = 0

for quest in questions:
    print("----------------------------------------")
    print(quest) #It was a singlr tuple so it was iterative over a for loop
    #Now along with each question we have to print an option 
    for option in options[question_num]: #we have considered here an index operator questio_num which has initial value as 0
        print(option) #This will print the same options for each queston
    
    guess = input("Enter your option (A,B,C,D) : ").upper()
    guesses.append(guess)
    if guess == answers[question_num]: #answer tuple at index of question number
        score+=1
        print("correct!")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is correct answer")

    question_num = question_num+1 #This will help to print the different options for each question

print("--------------------------------")
print("             RESULT             ")
print("--------------------------------")
print("answers:",end="")
for answer in answers:
    print(answer, end=" ")
print()

for guess in guesses:
    print(guess, end=" ")

score = int(score/int(len(questions)*100)) # If the answer is correct then the score variable is incrementing by 1
print(f"Your score is {score}%")

        
         