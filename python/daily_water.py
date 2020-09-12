class DailyWater:

    def __init__(self, gender):
        self.gender = gender

    def water_needed(self, water):

        if 'male' == lower(self.gender):
            self.water = 124
            print(self.water)

        if self.gender == lower('female'):
            self.water = 92

        return True



pipo = DailyWater('male')
print(pipo.gender)
