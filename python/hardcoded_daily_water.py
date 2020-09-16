
class DailyWaterIntake:

    def __init__(self, gender):
        self.gender = gender

    #
    # def gender(self):
    #     gender = input('Are you male or female: [m/f]')

    def neccessary_water(self):
        try:
            self.gender
            if self.gender.lower() == 'male':
                water = 124

            if self.gender.lower() == 'female':
                water = 92

        except Exception as arg:
            print('Error due to [{}]'.format(str(arg)))
            return False

        return 'You have entered {}. Therefore your daily water intake is {}oz.'.format(
            self.gender, water)

male = DailyWaterIntake('Female')
print(male.neccessary_water())

#
# def main():
#
#
#     waterintake = DailyWaterIntake()
#     if waterintake.neccessary_water() is False:
#         print('Unabale to calculatedaily water intake')
#         sys.exit(1)
#
#
#
# if __name__ == '__main__':
#     main()
