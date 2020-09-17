# def make_shirt(message, size):
    # print('\nThis is for shirt size {}.'.format(size))
    # print('This is the message on the shirt "{}".'.format(message))
#
# shirt_size = input('Please enter a shirt size [S,M,L,XL]: ')
# shirt_message = input('What do you want the shirt to say?: ')
#
# make_shirt(message=shirt_message, size=shirt_size)


def city_country(city, country):
    return '{}, {}.'.format(city, country)

# chosen_city = input('Please enter the city: ').title()
# chosen_country = input('Please enter the country: ').title()
#
# output = describe_city(city=chosen_city, country=chosen_country)
# print(output)

check = city_country('Santiago', "Chile")
dr_check = city_country('Santo Domingo', "Republica Dominicana")
rome = city_country('Rome', 'Italy')

print(check)
print(dr_check)
print(rome)
