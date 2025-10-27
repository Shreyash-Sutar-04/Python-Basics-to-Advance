# Quiz questions
questions = (
    "How many elements are in the periodic table? :",
    "Which animal lays the largest eggs? :",
    "What is the most abundant gas in Earth's atmosphere? :",
    "How many bones are in the human body? :",
    "Which planet in the solar system is the hottest?"
)

# Options for each question
options = (
    ("A. 116", "B. 118", "C. 117", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")
)

# Correct answers
answers = ("B", "D", "A", "A", "B")

# Initialize variables
guesses = []
score = 0
question_num = 0

# Loop through all questions
for question in questions:
    print("----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    # Take user input
    guess = input("Enter your answer (A, B, C, D): ").upper()
    guesses.append(guess)
    
    # Check answer
    if guess == answers[question_num]:
        print("✅ You got it right!")
        score += 1
    else:
        print("❌ Wrong!")
        print(f"Correct answer: {answers[question_num]}")
    
    question_num += 1

# Display results
print("\n---------------------------------")
print("              RESULT              ")
print("---------------------------------")

print("Answers: ", end="")
for ans in answers:
    print(ans, end=" ")

print("\nGuesses: ", end="")
for guess in guesses:
    print(guess, end=" ")

# Calculate percentage score correctly
score_percent = int((score / len(questions)) * 100)
print(f"\n\nYour final score is: {score_percent}%")
