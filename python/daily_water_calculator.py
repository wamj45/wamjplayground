
import sys

class DailyWaterIntake:

    def __init__(self, gender):
        self.gender = gender
        self.necessary_water = None
        self.water_drunk = None
        self.total_water_drunk = None
        self.bottle_water = None

    def amt_water_drunk(self):

        if self.water_bottles_drunk() is False:
            print('Unable to calculate how many water bottles were drunk')
            return False

        water_drank = int(input('Please enter the amount of water you have dranken today: '))

        if water_drank == 0:
            self.water_drunk = self.bottle_water
            print('Dang no water?!')

        else:
            self.water_drunk = self.bottle_water + water_drank

        return True

    def water_bottles_drunk(self):

        water_bottle = 16.9
        bottles_drank = int(input('Please enter how many water bottles you have drunken from: '))
        if bottles_drank == 0:
            print('Ok cool no water bottles for you :)')
            self.bottle_water = 0
        else:
            amt_water_from_bottles = bottles_drank * water_bottle
            print('That equates to {:.2f}oz'.format(amt_water_from_bottles))

            self.bottle_water = amt_water_from_bottles

        return True

    def neccessary_water(self):

        try:
            self.gender

            if self.gender.lower() == 'male':
                self.necessary_water = 124

            if self.gender.lower() == 'female':
                self.necessary_water = 92
        except Exception as arg:
            print('Error due to [{}]'.format(str(arg)))
            return False

        return True

    def total_water(self):

        if self.amt_water_drunk() is False:
            print('Unable to initialize program')
            return False

        if self.neccessary_water() is False:
            print('Unable to calculate your necessary daily water intake')
            return False

        self.total_water_drunk = self.water_drunk - self.necessary_water

        if self.total_water_drunk < 0:
            water_needed = self.total_water_drunk * (-1)
            print('You should still drink {:.2f}oz of water'.format(water_needed))

        elif self.total_water_drunk >= 0:
            print('You drank enough water for today!')
            print('You are {}oz over your daily needs'.format(self.total_water_drunk))

        return True

def main():

    user = input('Please enter the gender you identify most with(male/female): ')
    water_test = DailyWaterIntake(gender=user)

    if water_test.total_water() is False:
        print('Unable to calculate the neccesart water intake for you')
        sys.exit(1)

    print('Done!')
    sys.exit(0)

if __name__ == "__main__":
    main()
