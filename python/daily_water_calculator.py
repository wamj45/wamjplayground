
import sys

#need to add a variable which wil hold all of the water drunk for a day
# go back an rename these variable sthey are too similar and it is confusing
class DailyWaterIntake:

    def __init__(self, gender):
        self.gender = gender
        self.daily_water = ''
        self.water_drunk = 0
        self.total_water_drunk = 0

    def amt_water_drunk(self):
        #need to fadd a False check
        water_drank = int(input('Please enter the amount of water you have dranken today: '))

        if water_drank == 0:
            print('Dang no water?!')

        else:
            self.water_drunk = self.water_drunk + water_drank
            # Call the self.total_water_drunk here and create its amt of water

        return True

    def water_bottles_drunk(self):
        #need to add a False statement in theis method
        water_bottle = 16.9
        bottles_drank = int(input('Please enter how many water bottles you have drunken from: '))
        if bottles_drank == 0:
            print('Ok cool no water bottles for you :)')
        else:
            amt_water_from_bottles = bottles_drank * water_bottle
            print('That equates to {:.2f}'.format(amt_water_from_bottles))
            # Water the heck is this variable 'self.water'?
            # TODO:
            # create a new list and function which contains the total amt of
            # water drank in hte day
            self.water = amt_water_from_bottles

        return True

    def neccessary_water(self):

        if self.water_bottles_drunk() is False:
            print('So you did not drink from a water bottle today. Cool.')
            return False

        try:
            self.gender

            if self.gender.lower() == 'male':
                self.daily_water = 124

            if self.gender.lower() == 'female':
                self.daily_water = 92
        except Exception as arg:
            print('Error due to [{}]'.format(str(arg)))
            return False
        #Need to edit this print statement. the you have enterd part is kinda
        #weird as the program expands
        print('You have entered {}. Therefore your daily water intake is {} oz.'.format(
            self.gender, self.daily_water))

        if self.amt_water_drunk() is False:
            print("So you have not drinken any water today, that's OK fam!")
            return False

        else:
            # Think about what you want to put here. We can have it just return
            # True, nonething at all, ie remove the else statement, or have it print
            # put something


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
