import random

# Function to display a question and check answer
def ask_question(question_data):
    print("\n" + question_data["question"])
    for option in question_data["options"]:
        print(option)
    answer = input("Enter your answer (A/B/C/D): ").strip().upper()
    if answer == question_data["answer"]:
        print("✅ Correct!")
        return True
    else:
        print(f"❌ Wrong! The correct answer was {question_data['answer']}.")
        return False

# Main game function
def quiz_game():
    print("🎮 Welcome to the Python Trivia Quiz!")
    print("--------------------------------------")

    # Question bank
    questions = [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A) func", "B) define", "C) def", "D) function"],
            "answer": "C"
        },
        {
            "question": "What is the output of: print(type([]))?",
            "options": ["A) <class 'list'>", "B) <class 'dict'>", "C) <class 'tuple'>", "D) <class 'set'>"],
            "answer": "A"
        },
        {
            "question": "Which module is used to generate random numbers in Python?",
            "options": ["A) random", "B) math", "C) time", "D) os"],
            "answer": "A"
        },
        {
            "question": "What is the correct syntax to output 'Hello World' in Python?",
            "options": ["A) echo('Hello World')", "B) print('Hello World')", "C) printf('Hello World')", "D) println('Hello World')"],
            "answer": "B"
        },
        {
            "question": "Which data type is immutable in Python?",
            "options": ["A) List", "B) Dictionary", "C) Tuple", "D) Set"],
            "answer": "C"
        }
    ]

    random.shuffle(questions)  # Randomize question order
    score = 0

    for question_data in questions:
        if ask_question(question_data):
            score += 1

    print("\n🎯 Quiz Over!")
    print(f"Your Final Score: {score}/{len(questions)}")

    if score == len(questions):
        print("🏆 Excellent! You are a Python Pro!")
    elif score >= len(questions) // 2:
        print("👍 Good Job! Keep Learning.")
    else:
        print("📘 Better luck next time!")

# Run the game
quiz_game()
