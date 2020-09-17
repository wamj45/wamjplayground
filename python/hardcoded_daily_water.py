
# class DailyWaterIntake:
#will add class capability after making the function version work
#
# def __init__(self, gender):
#     self.gender = gender

def user_gender(self):
    return self.gender

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

entered_gender = input('Please enter your gender[m/f]: ')

check = user_gender(entered_gender)
