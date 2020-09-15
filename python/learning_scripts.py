def make_shirt(size, message):
    print('\nThis is for shirt size {}.'.format(size))
    print('This is the message on the shirt "{}".'.format(message))

# make_shirt('L', 'Red Sox')
shirt_size = input('Please enter a shirt size [S,M,L,XL]: ')
shirt_message = input('What do you want the shirt to say?: ')

make_shirt(size=shirt_size, message=shirt_message)
