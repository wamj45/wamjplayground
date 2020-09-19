import sys


class DailyWaterIntake:

    def __init__(self, gender):
        self.gender = gender
        self.water_needed = ''

    def water_bottles_drunk(self):

        water_bottle = 16.9
        drank = int(input('Please enter how many water bottles you have drunken from: '))
        if drank == 0:
            print('Ok cool no water bottles for you :)')
        else:
            amt_water_from_bottles = drank * water_bottle
            print('That equates to {}'.format(amt_water_from_bottles))


        return True

    def neccessary_water(self):

        if self.water_bottles_drunk() is False:
            print('So you did not drink from a water bottle today. Cool.')
            return False

        try:
            self.gender
            if self.gender.lower() == 'male':
                self.water_needed = 124
            if self.gender.lower() == 'female':
                self.water_needed = 92
        except Exception as arg:
            print('Error due to [{}]'.format(str(arg)))
            return False
        #Need to edit this print statement. the you have enterd part is kinda
        #weird as the program expands
        print('You have entered {}. Therefore your daily water intake is {} oz.'.format(
            self.gender, self.water_needed))

        return True


def main():

    user = input('Please enter the gender you identify most with(male/female): ')
    water_test = DailyWaterIntake(gender=user)

    if water_test.neccessary_water() is False:
        print('Unable to calculate the neccesart water intake for you')
        sys.exit(1)

    print('Done!')
    sys.exit(0)

if __name__ == "__main__":
    main()
