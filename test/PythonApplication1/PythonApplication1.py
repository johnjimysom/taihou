print("Hello World ")
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
hero_name= input('who is your favorite hero? ')
print('hello ' + name + ' your favorite hero name is ' + hero_name)