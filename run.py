print("Welcom in ArabiaChallenge \n")
from questions import questions

def get_question(ques_num):
    """
    Get Question from questions sheet
    """
    question_data = questions[ques_num]
    print(question_data["question"])
    for choice in question_data["choices"]:
        print(choice)


def request_answer():
    player_answer = input("Your answer (1, 2, 3, or 4): ").strip()

    if validate_answer(player_answer):
        print('Data is valid')
        
    return player_answer


def validate_answer(player_answer):
    valid_answers = ['1', '2', '3', '4']
    while player_answer not in valid_answers:
        print("Invalid input. Please enter 1, 2, 3, or 4.")
    print(player_answer)


get_question(1)
request_answer()
