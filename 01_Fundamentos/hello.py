print('Hello world')
print('what is your name?') # pregunta por el nombre
my_name = input('>')

print('Hi ' + my_name + ', nice to meet you')

print('The length of your name is: ' + str(len(my_name))) #str(len(var))

print('What is your age?')
my_age = input('>')
print('You will be ' + str(int(my_age) + 1) + ' in a year.') # parse str to int
