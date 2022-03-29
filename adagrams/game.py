import random
import copy

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

# build a hand of 10 letters
def draw_letters():
    draw_pool = []
    # create a list based on LETTER_POOL
    for key, value in LETTER_POOL.items():
        draw_pool.extend([key]*value)
    # create hand with sample of random letters from draw_pool
    hand = random.sample(draw_pool, 10)
    return(hand)

def uses_available_letters(word, letter_bank):
    available_letters = letter_bank.copy()
    for letter in word:
        letter = letter.upper()
        if letter in available_letters:
            available_letters.remove(letter)
        else:
            return False
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass


draw_letters()