# work with the preset variable `words`
def start_with_letter(word: str, letter: str):
    first_letter = word[0]
    starts_with_letter = first_letter.upper() == letter.upper()
    if starts_with_letter:
        return True
    else:
        return False


starting_with_a = [word for word in words if start_with_letter(word, 'A')]
print(starting_with_a)
