import random
import sys
# This program should give the user two problems for each of the following
# operations to solve:
# +,-,*,/ and %
# each of the math operations should have its own function

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

        print('You got {} questions right'.format(self.add_score))

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

        print('You got {} questions right'.format(self.sub_score))

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

        print('You got {} questions right'.format(self.multiply_score))

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

        print('You got {} questions right'.format(self.divide_score))

        return True

    def modulus_questions(self):

        return True

    def calculate_score(self):

        if self.addition_questions() is False:
            print('Error - Unable to load the addition portion of the quiz')

        if self.subtraction_questions() is False:
            print('Error - Unable to load the subtraction questions')

        if self.multiplication_questions() is False:
            print('Error - Unable to load the multiplication questions')

        if self.division_questions() is False:
            print('Error - Unable to load the division_questions')

        return True

def main():

    quiz = MathQuiz()
    if quiz.calculate_score() is False:
        print('Error - Unable to load quiz')
        sys.exit(1)

    # Need to add a run back option
    print('Done!')

if __name__ == '__main__':
    main()
