print("Welcom in ArabiaChallenge \n")
from questions import questions
import arabic_reshaper
from bidi.algorithm import get_display


def reshape_text(text):
    """
    Correct Arabic typo from right to left 
    """
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text


def get_question(ques_num):
    """
    Get Question from questions sheet
    """
    question_data = questions[ques_num]  
    print(reshape_text(question_data["question"])) # Apply reshap_text with quistion
    for choice in question_data["choices"]:
        print(reshape_text(choice))  # Apply reshap_text with choice
    return question_data


def request_answer():
    """
    Request answer from input 
    """
    while True:
        print('Please enter your answer. \n')
        player_answer = input("Your answer: \n").strip()

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
    """
    Compare user answer with right answer, 
    Print massage with correct answer if it wrong.
    Increase score if it right, 
    """
    if player_answer == correct_answer:
        score += 1
        print("Correct ! \n")
            
    else:
        print(f"Wrong. The correct answer is {correct_answer}. \n")
    print(f"Your Score : {score}. \n")
    return score


# def score_collector(compare_answer, score):
#     if True:
#         return 1
#         print(f"Your Score : {score}")   
#     else:
#         return 0
def final_score(total_ques, score):
    """
    Print the final score after all questions are answered
    """
    
    print(f"Your final score :\n \n {score} out of {total_ques}. \n")


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
    
    final_score(len(questions), score)
        

        

main()