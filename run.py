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
    """
    Validate answers, If the input answer not in 1, 2, 3 or 4 rise
    Invalid input error 
    """
    valid_answers = ['1', '2', '3', '4']
    if player_answer not in valid_answers:
        print("Invalid input. Please enter 1, 2, 3, or 4.")
        return False
    return True


def compare_answer(player_answer, correct_answer, score):
    if player_answer == correct_answer:
        score += 1
        print("Correct !")
            
    else:
        print(f"Wrong. The correct answer is {correct_answer}.")
    print(f"Your Score : {score}")
    return score


# def score_collector(compare_answer, score):
#     if True:
#         return 1
#         print(f"Your Score : {score}")   
#     else:
#         return 0
    


def main():
    """
    Run all programm functions
    """
    score = 0

    for i in range(len(questions)):
        question_data = get_question(i)  
        player_answer = request_answer()
        score = compare_answer(player_answer, question_data["answer"], score)
        # score_collector(compare_answer, score)
        # score = score_collector(compare_answer, score)

        

main()