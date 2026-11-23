import random

questions = [
    {
        "q": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. define", "C. def", "D. function"],
        "ans": "C"
    },
    {
        "q": "What is the output of type([]) in Python?",
        "options": ["A. tuple", "B. list", "C. dict", "D. set"],
        "ans": "B"
    },
    {
        "q": "Which data structure follows LIFO?",
        "options": ["A. Queue", "B. Linked List", "C. Stack", "D. Tree"],
        "ans": "C"
    },
    {
        "q": "What does HTTP stand for?",
        "options": [
            "A. HyperText Transfer Protocol",
            "B. High Text Transfer Program",
            "C. HyperText Transmission Path",
            "D. None of the above"
        ],
        "ans": "A"
    },
    {
        "q": "Which operator is used for floor division in Python?",
        "options": ["A. /", "B. %", "C. //", "D. **"],
        "ans": "C"
    }
]

def run_quiz():
    random.shuffle(questions)
    score = 0

    for i, item in enumerate(questions, 1):
        print(f"\nQ{i}. {item['q']}")
        for opt in item["options"]:
            print(opt)

        user_ans = input("Your answer (A/B/C/D): ").strip().upper()
        if user_ans == item["ans"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer was {item['ans']}")

    percent = (score / len(questions)) * 100
    print(f"\nFinal Score: {score}/{len(questions)} ({percent:.1f}%)")

if __name__ == "__main__":
    run_quiz()