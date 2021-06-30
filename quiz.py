from question import question
question_prompts = [
    "what color are apples?\n(a) red\n(b) green\n(c) purple\n\n",
    "what color are bananas?\n(a) magenta\n(b) teal\n(c) yellow\n\n",
    "what color are pineapple?\n(a) blue\n(b) yellow\n(c) green\n\n",
]

questions = [
    question(question_prompts[0], "a"),
    question(question_prompts[1], "c"),
    question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompts)
        if answer == question.answer:
            score += 1
    print("you got " + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)