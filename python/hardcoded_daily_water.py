
class DailyWaterIntake:

    def __init__(self, water):
        self.gender = gender
        self.water = None

    def gender(self):
        gender = input('Are you male or female: [m/f]')


    def neccessary_water(self, water):
        try:
            self.gender

            if self.gender == 'm':
                print('you have entered male')
                self.water = 124
                print(self.water)

            if self.gender == 'f':
                print('you have etered female')
        except Exception as arg:
            print('Error due to [{}]'.format(str(arg)))
