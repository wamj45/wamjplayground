import sys


class DailyWaterIntake:

    def __init__(self, gender):
        self.gender = gender

    def user_gender(self):
        return gender

    def neccessary_water(self):

        water = ''
        try:
            self.gender
            if self.gender.lower() == 'male':
                water = 124


            if self.gender.lower() == 'female':
                water = 92

        except Exception as arg:
            print('Error due to [{}]'.format(str(arg)))
            return False

        print('You have entered {}. Therefore your daily water intake is {} oz.'.format(
            self.gender, water))

        return True


def main():

    user = input('Please enter your gender[m/f]: ')
    water_test = DailyWaterIntake(gender=user)

    if water_test.neccessary_water() is False:
        print('Unable to calculate the neccesart water intake for you')
        sys.exit(1)

    print('Done!')
    sys.exit(0)

if __name__ == "__main__":
    main()
