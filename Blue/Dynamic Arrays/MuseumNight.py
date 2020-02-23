import string
string.ascii_lowercase
alphabet_arr = list(string.ascii_lowercase)

input_letter = input()


def convert_number(letter):
    total = 0
    current_index = 0

    split_text = list(letter.lower())

    for i in range(len(split_text)):
        letter_index = alphabet_arr.index(split_text[i])
        remain = abs(letter_index - current_index)
        current_index = letter_index
        if (remain > 13):
            value = 26 - remain
            total += value
        else:
            total += remain
    print(total)


convert_number(input_letter)
