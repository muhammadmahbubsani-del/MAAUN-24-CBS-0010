# Step 1: Setup - list of dictionaries
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "correct_answer": "C"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["A. Python", "B. JavaScript", "C. C++", "D. Java"],
        "correct_answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Process Unit",
            "B. Central Processing Unit",
            "C. Computer Personal Unit",
            "D. Central Processor Utility"
        ],
        "correct_answer": "B"
    }
]

# Step 5: Function to calculate percentage
def calculate_percentage(score, total):
    return (score / total) * 100

# Step 2–4: Execute, Interact, Evaluate
score = 0

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer == q["correct_answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct answer is {q['correct_answer']}")

# Final Output
total_questions = len(questions)
percentage = calculate_percentage(score, total_questions)

print("\nQuiz Completed!")
print(f"Your Score: {score}/{total_questions}")
print(f"Percentage: {percentage:.2f}%")

if percentage >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")