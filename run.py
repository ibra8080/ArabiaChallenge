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

get_question(0)