import random
def generate_new_random() -> str:
    number = "0"
    while not valid_guess(number):
        number = str(random.randint(1023, 9876))
    return number

def valid_guess(guess: str) -> bool:
    if not guess.isdigit():
        return False
    if len(guess) != 4:
        return False
    if guess[0] == '0':
        return False
    if len(set(guess)) != len(guess):
        return False
    return True

def count_codes(guess: str, secret_number: str) -> int:
    """
    The function counts the positions where the digits of the secret number and the human guess are the same.
    :param guess:
    :param secret_number:
    :return:
    """
    guess = str(guess)
    count = 0
    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            count += 1
    return count



def count_runners(guess: str, secret_number: str) -> int:
    """
    The function counts how many digits from the human guess show up in the secret number, but not on the same position as the specified digit in the human choice
    :param guess:
    :param secret_number:
    :return:
    """
    guess = str(guess)
    count = 0
    for i in range(len(guess)):
        for j in range(len(secret_number)):
            if guess[i] == secret_number[j] and i != j:
                count += 1
    return count


def is_won_by_human(guess: str, secret_number: str) -> bool:
    if guess == secret_number:
        return True
    else:
        return False








