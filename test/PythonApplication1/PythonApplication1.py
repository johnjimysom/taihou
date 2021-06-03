print("Hello Wolo ")
a = [1, 2 , 6, 99]
a.sort()
print(a)

#working order of tuple
numbers_tuple = (6, 9, 3, 1)
numbers_set = {5, 5, 10, 1, 0}
numbers_tuple_sorted = sorted(numbers_tuple)
numbers_set_sorted = sorted(numbers_set)
print(numbers_tuple_sorted)
print(numbers_set_sorted) 


b = {12,33,33,22,14,545}
print(b) 


cars = ['Ford', 'BMW', 'Volvo', 'Honda']
cars.sort()
print(cars)

names = ['Harry', 'Suzy', 'Al', 'Mark']
sorted_characters = sorted(names)
sorted(names, reverse=False)
print(sorted_characters )


different_lengths = ['hhhh', 'hh', 'hhhhh','h']
sorted(different_lengths)
print(different_lengths)

name = input('who are you? ')
hero_name= input('who is your favorite heroic servant in FGO? ')
print('hello ' + name + ' your favorite heroic servant is ' + hero_name)

birth_year = input('birth year: ')
print(type(birth_year))
int(birth_year)
age = 2021 - int(birth_year)
print(type(age))
print(age)

#ask a user their weight (in pounds), convert it to kilograms and print on the terminal

weight_lbs = input('Weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

course = "Python's hair is a cool in Girl's Frontline"
course2 = 'Python is a cool in "GFL"'
course3 = '''
Hi John,

Herr ist sie email du dich,

Danke,
The cool guys

'''
print(course +' :[course]')
print(course2 +' :[course2]')
print('[course3]:' + course3)

#to use array or call from an array..
print('starting from the variable course[0] to [3] goes to: '+ course[0:3])
print('starting from the variable course[1:] to goes to the end: '+ course[1:])
print('starting from the variable course[:5] to goes to the end: '+ course[:5])
print('starting from the variable course[0] the course[4] goes to: '+ course[4])
print('starting from the variable course[0] the course[-1] goes to the end of the sentence: '+ course[-1])
another = course[:]
print('course[:] clones a string: '+ course[:])

name2 = "Johnjimy"
print('name2[1:-1] omits the first letter J and -1 omits the y: '+name2[1:-1])

#lets look at formatted Strings