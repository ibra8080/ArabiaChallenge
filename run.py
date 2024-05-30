import os
import random
import colorama
from colorama import Fore, Back, Style
from questions import questions
import arabic_reshaper
from bidi.algorithm import get_display


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


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
    print(reshape_text(question_data["question"]))  # Apply reshap_text
    for choice in question_data["choices"]:
        print(reshape_text(choice))   # Apply reshap_text with choice
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
        print(
            Fore.RED 
            + f"{player_answer} is invalid. Please enter 1, 2, 3, or 4.")
        return False
    return True


def compare_answer(player_answer, correct_answer, score):
    """
    Compare user answer with right answer,
    Print massage with correct answer if it wrong.
    Increase score if it right.
    """
    clear()
    if player_answer == correct_answer:
        score += 1
        print(Fore.GREEN + "Correct ! \n")

    else:
        print(Fore.CYAN + f"Wrong. The correct answer is {correct_answer}. \n")
    print(f"Your Score : {score}. \n")
    return score


def final_score(total_ques, score):
    """
    Print the final score after all questions are answered
    """
    print(
        f"Your final score :\n{Back.GREEN}{Style.
        BRIGHT}{score} out of {total_ques}. \n")


def asking_replay():
    """
    asking the player for replay or to end the game
    """
    while True:
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay in ['yes', 'no']:
            return replay
        else:
            print(Fore.RED + "Invalid input. Please enter 'yes' or 'no'.")


def main():
    """
    Run all programm functions
    """

    while True:
        score = 0
        random.shuffle(questions)

        for i in range(len(questions)):
            question_data = get_question(i)
            player_answer = request_answer()
            score = compare_answer(
                player_answer, question_data["answer"], score)

        final_score(len(questions), score)

        if asking_replay() == "no":
            print(Fore.YELLOW + "Thank you for playing. Goodbye!")
            break




if __name__ == "__main__":
    clear()
    colorama.init(autoreset=True)
    print(Fore.YELLOW + "Welcome in ArabiaChallenge \n")
    main()
