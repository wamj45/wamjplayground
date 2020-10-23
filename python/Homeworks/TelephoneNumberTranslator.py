#**********************  math_quiz.py  *********************
#
# Name: Wilbert A Martinez Jr
#
# Course: CSCI 1470
#
# Assignment: Homework #2
#
# Algorithm
#   Prompt user for telephone number
#   Remove dashes from input
#   collect the area code of number
#   Convert letters to numbers
#   Reconstruct phone number
#   Output phone number to user
#   Ask user to continue
#**********************************************************


import sys

class Translator:

    def __init__(self, input):
        self.no_dashes = None
        self.area_code = None
        self.letters = None
        self.numbers = ''
        self.input = input

    def remove_dashes(self):
        if '-' in self.input:
            self.no_dashes = self.input.replace('-', '')
        return True

    def get_area_code(self):

        if self.remove_dashes() is False:
            print('Error')
            return False

        self.area_code = self.no_dashes[:3]
        self.letters = self.no_dashes[3:11]

        return True

    def letter_to_numbers(self):

        if self.get_area_code() is False:
            print('Error')
            return False

        for num in self.letters:
            if num == 'A' or num == 'B' or num == 'C':
                num = '2'
                self.numbers = self.numbers + num
            if num == 'D' or num == 'E' or num == 'F':
                num = '3'
                self.numbers = self.numbers + num
            if num == 'G' or num == 'H' or num == 'I':
                num = '4'
                self.numbers = self.numbers + num
            if num == 'J' or num == 'K' or num == 'L':
                num = '5'
                self.numbers = self.numbers + num
            if num == 'M' or num == 'N' or num == 'O':
                num = '6'
                self.numbers = self.numbers + num
            if num == 'P' or num == 'Q' or num == 'R':
                num = '7'
                self.numbers = self.numbers + num
            if num == 'T' or num == 'U' or num == 'V':
                num = '8'
                self.numbers = self.numbers + num
            if num == 'W' or num == 'X' or num == 'Y' or num == 'Z':
                num = '9'
                self.numbers = self.numbers + num

        return True

    def phone_number(self):

        if self.letter_to_numbers() is False:
            print('Error')
            return False
        mid_digits = self.numbers[:3]
        last_four_digits = self.numbers[3:7]
        print('Here is your translated number: [{}-{}-{}]'.format(self.area_code,
            mid_digits, last_four_digits))

        return True

def main():
    user_input = str(input('Please enter [q] to quit. Else, enter a phone number to translate: '))


    while user_input != 'q':

        translate = Translator(user_input)
        if translate.phone_number() is False:
            print('This no work')

        user_input = str(input('Please enter [q] to quit. Else, enter a phone number to translate: '))



    if user_input == 'q':
        print('Goodbye!')
        sys.exit(0)


if __name__ == '__main__':
  main()
