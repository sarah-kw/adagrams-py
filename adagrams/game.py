import random

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

LETTER_VALUES = {
    "A" : 1, "E" : 1, "I" : 1, "O" : 1, "U" : 1,
    "L" : 1, "N" : 1, "R" : 1, "S" : 1, "T" : 1, 
    "D" : 2, "G" : 2,
    "B" : 3, "C" : 3, "M" : 3, "P" : 3,
    "F" : 4, "H" : 4, "V" : 4, "W" : 4, "Y" : 4,
    "K" : 5,
    "J" : 8, "X" : 8,
    "Q" : 10,"Z" : 10
    }

LONG_WORD_BONUS = 8
LONG_WORD_RANGE = (7, 8, 9, 10)

DRAW_POOL = [key for key, value in LETTER_POOL.items() for value in range(value)]

# build a hand of 10 letters
def draw_letters():
    hand = random.sample(DRAW_POOL, 10)
    return hand

def uses_available_letters(word, letter_bank):
    available_letters = letter_bank.copy()
    word = word.upper()
    for letter in word:
        if letter in available_letters:
            available_letters.remove(letter)
        else:
            return False
    return True

# scores word based on letter values, bonus of 8 points added for words 7-10 letters long
def score_word(word):
    score = 0
    word = word.upper()
    for letter in word:
        if letter in LETTER_VALUES:
            score += LETTER_VALUES[letter]
        else:
            continue
    if len(word) in LONG_WORD_RANGE:
        score += LONG_WORD_BONUS

    return score

def get_highest_word_score(word_list):
    word_dict = {word:score_word(word) for word in word_list}

    highest_scoring_word = max(word_dict, key=word_dict.get)
    high_score = word_dict[highest_scoring_word]

    for word,score in word_dict.items():
        if score == high_score:
            if len(word) == 10:
                highest_scoring_word = word
                break
            elif len(word) < len(highest_scoring_word):
                highest_scoring_word = word

    return tuple([highest_scoring_word, high_score])
