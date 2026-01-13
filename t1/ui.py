from t1.functions import *

def print_menu():
    print("""
==================================================
            CODE GUESSING GAME
-> Try to guess the 4-digit secret number
-> Enter 8086 to reveal the secret number     
=================================================""")

def start():
    print_menu()
    random_number_to_guess = generate_new_random()
    while True:
        human_choice = str(input("Enter a 4-digit number: "))
        if human_choice == "8086":
            print("The secret number is" , random_number_to_guess)
            continue
        if not valid_guess(human_choice):
            print("Invalid guess. The computer wins")
            print("The secret number was", random_number_to_guess)
            break
        if is_won_by_human(human_choice, random_number_to_guess):
            print("You guessed the secret number. Congratulations!")
            break
        codes = count_codes(human_choice, random_number_to_guess)
        runners = count_runners(human_choice, random_number_to_guess)
        print("Codes:", codes)
        print("Runners:", runners)



