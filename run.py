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
    return question_data


def request_answer():
    """
    Request answer from input 
    """
    while True:
        print('Please enter your answer.')
        player_answer = input("Your answer: ").strip()

        if validate_answer(player_answer):
            break
    return player_answer


def validate_answer(player_answer):
    valid_answers = ['1', '2', '3', '4']
    if player_answer not in valid_answers:
        print("Invalid input. Please enter 1, 2, 3, or 4.")
        return False
    return True


def compare_answer(player_answer, correct_answer):
    if player_answer == correct_answer:
        print("Correct !")
    else:
        print(f"Wrong. The correct answer is {correct_answer}.")


def main():
    for i in range(len(questions)):
        question_data = get_question(i)  
        player_answer = request_answer()
        compare_answer(player_answer, question_data["answer"])
 
        

main()