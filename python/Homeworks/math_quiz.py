#**********************  math_quiz.py  *********************
#
# Name: Wilbert A Martinez Jr
#
# Course: CSCI 1470
#
# Assignment: Homework #1
#
# Algorithm
#   Prompt user to start the quiz
#   Generate Math quiz starting with addition questions
#   Continue with subtraction, multiplication, division, then modulus questions
#   Calulate final score and output it
#**********************************************************

import random
import sys

class MathQuiz:

    def __init__(self):
        self.add_score = 0
        self.sub_score = 0
        self.multiply_score = 0
        self.divide_score = 0
        self.mod_score = 0

    def addition_questions(self):

        add1 = random.randint(1,20)
        add2 = random.randint(1,20)
        add3 = random.randint(1,20)
        add4 = random.randint(1,20)

        ans1 = add1 + add2
        ans2 = add3 + add4

        user_entry1 = int(input('{} + {} = '.format(add1, add2)))
        user_entry2 = int(input('{} + {} = '.format(add3, add4)))

        if ans1 == user_entry1:
            self.add_score += 1

        if ans2 == user_entry2:
            self.add_score += 1

        return True

    def subtraction_questions(self):

        sub1 = random.randint(1,20)
        sub2 = random.randint(1,20)
        sub3 = random.randint(1,20)
        sub4 = random.randint(1,20)

        ans3 = sub1 - sub2
        ans4 = sub3 - sub4

        user_entry3 = int(input('{} - {} = '.format(sub1, sub2)))
        user_entry4 = int(input('{} - {} = '.format(sub3, sub4)))

        if ans3 == user_entry3:
            self.sub_score += 1

        if ans4 == user_entry4:
            self.sub_score += 1

        return True

    def multiplication_questions(self):

        mult1 = random.randint(1,20)
        mult2 = random.randint(1,20)
        mult3 = random.randint(1,20)
        mult4 = random.randint(1,20)

        ans5 = mult1 * mult2
        ans6 = mult3 * mult4

        user_entry5 = int(input('{} * {} = '.format(mult1, mult2)))
        user_entry6 = int(input('{} * {} = '.format(mult3, mult4)))

        if ans5 == user_entry5:
            self.multiply_score += 1

        if ans6 == user_entry6:
            self.multiply_score += 1

        return True

    def division_questions(self):

        div1 = random.randint(1,20)
        div2 = random.randint(1,20)
        div3 = random.randint(1,20)
        div4 = random.randint(1,20)

        ans7 = div1 // div2
        ans8 = div3 // div4

        user_entry7 = int(input('{} // {} = '.format(div1, div2)))
        user_entry8 = int(input('{} // {} = '.format(div3, div4)))

        if ans7 == user_entry7:
            self.divide_score += 1

        if ans8 == user_entry8:
            self.divide_score += 1

        return True

    def modulus_questions(self):

        mod1 = random.randint(1,20)
        mod2 = random.randint(1,20)
        mod3 = random.randint(1,20)
        mod4 = random.randint(1,20)

        ans9 = mod1 % mod2
        ans0 = mod3 % mod4

        user_entry9 = int(input('{} % {} = '.format(mod1, mod2)))
        user_entry0 = int(input('{} % {} = '.format(mod3, mod4)))

        if ans9 == user_entry9:
            self.mod_score += 1

        if ans0 == user_entry0:
            self.mod_score += 1

        return True

    def calculate_score(self):

        if self.addition_questions() is False:
            print('Error - Unable to load the addition portion of the quiz')

        if self.subtraction_questions() is False:
            print('Error - Unable to load the subtraction questions')

        if self.multiplication_questions() is False:
            print('Error - Unable to load the multiplication questions')

        if self.division_questions() is False:
            print('Error - Unable to load the division questions')

        if self.modulus_questions() is False:
            print('Error - Unable to load the modulus questions')

        total_score = self.divide_score + self.add_score + self.sub_score + self.multiply_score + self.mod_score
        percentage = total_score * 10
        print('You answered {} questions correctly. You scored a {}'.format(total_score, percentage))

        return True

def main():

    start_msg = 'Please enter [q] to quit the quiz. Otherwise, enter any key to coninue: '
    user_input = str(input(start_msg))


    while user_input != 'q':
        quiz = MathQuiz()
        if quiz.calculate_score() is False:
            print('Error - Unable to load quiz')
        print('Done!')
        user_input = str(input(start_msg))

    if user_input == 'q':
        print('Goodbye')
        sys.exit(0)



if __name__ == '__main__':
    main()
