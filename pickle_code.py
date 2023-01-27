
import pickle
import sys

TRANSLATION = {'0': '', '1': '',
               '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}


def read_orders(filename):
    open_order_numbers = open(filename, 'rb')
    order_numbers_set = pickle.load(open_order_numbers)
    open_order_numbers.close()
    return order_numbers_set


def read_words(filename):
    open_words = open(filename, 'r')
    word_list = open_words.readlines()
    new_words = []
    for word in word_list:
        new_words.append(word.strip('\n'))
    open_words.close()
    return new_words


def find_all_possible_combinations(order_number):
    all_combos = []
    for num in order_number:
        all_combos = add_digit(num, all_combos)
    return all_combos


def add_digit(digit, combinations):
    combos = []
    if combinations == []:
        for x in TRANSLATION[digit]:
            combos.append(x)
        return combos
    else:
        for x in combinations:
            for y in TRANSLATION[digit]:
                combos.append(x+y)
        return combos


def filter_valid_words(possbile_combinations, valid_words):
    filtered_words = []
    for word in possbile_combinations:
        if word in valid_words:
            filtered_words.append(word)
    return filtered_words


def display_possible_words(order_number, words):
    if words == []:
        print('\n' + order_number.strip() + ' : No real word found.')
    else:
        print('\n' + order_number.strip() + ' : ' + words[0])
        for word in words[1:]:
            print(f"{word:>13}")


def main():
    try:
        first_argument = sys.argv[1]
        second_argument = sys.argv[2]
        order_file = read_orders(first_argument)
        word_file = read_words(second_argument)
    except FileNotFoundError:
        print('Error: There was a problem with at least one of the files.')
        sys.exit()
    for num in order_file:
        combos = find_all_possible_combinations(num)
        filtered_combos = filter_valid_words(combos, word_file)
        display_possible_words(num, filtered_combos)


if __name__ == '__main__':
    main()
