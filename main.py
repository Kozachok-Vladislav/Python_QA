#3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3

#3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#   - получите сумму всех чисел,
#   - распечатайте все строки, где есть буква 'a'

#3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж

#3.4. Напишите программу, которая определяет, какая семья больше.
      #1) Программа имеет два input() - например, family_1, family_2.
      #2) Членов семьи нужно перечислить через запятую.
     #Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

#3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
    #о вашем любимом фильме.
    #- распечатайте только ключи
    #- распечатайте только значения
    #- распечатайте пары ключ - значение

#3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

#3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]

#3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#     - найдите значения, которые встречаются в обоих множествах
#    - найдите значения, которые не встречаются в обоих множествах
#     - проверьте являются ли эти множества подмножествами друг друга



#3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3


"""my_list = ['a', 'b', [1, 2, 3], 'd']
for el in my_list[2]:
    print (el)
"""

#3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#   - получите сумму всех чисел,
#   - распечатайте все строки, где есть буква 'a'


"""list_1 = ['Hi', 'pineapple', 2, None, 75, 'pizza', 36, 100]

sum_of_numbers = sum(num for num in list_1 if isinstance(num, int) or isinstance(num, float))

print("The sum of all numbers in the list is:", sum_of_numbers)

print("All strings that contain the letter 'a' are:")
for string in list_1:
    if isinstance(string, str) and 'a' in string:
        print(string)
"""


#3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж

"""my_list = ['cat', 'dog', 'horse', 'cow']
this_is_tuple = tuple(my_list)
print(this_is_tuple)
"""


#3.4. Напишите программу, которая определяет, какая семья больше.
      #1) Программа имеет два input() - например, family_1, family_2.
      #2) Членов семьи нужно перечислить через запятую.
#Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')



"""family_1 = input("Enter family 1 members separated by commas: ").split(",")

family_2 = input("Enter family 2 members separated by commas: ").split(",")

num_members_1 = len(family_1)
num_members_2 = len(family_2)

if num_members_1 > num_members_2:
    print("Family 1 has more members")
elif num_members_2 > num_members_1:
    print("Family 2 has more members")
else:
    print("Equal")
"""


#3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
    #о вашем любимом фильме.
    #- распечатайте только ключи
    #- распечатайте только значения
    #- распечатайте пары ключ - значение



"""film = {
    "title": "Avatar",
    "director": "James Cameron",
    "year": 2009,
    "budget": 237000000,
    "main_actor": "Sam Worthington",
    "slogan": "Enter the World of Pandora."
}

print(film.keys())
print(film.values())
print(film.items())
"""


#3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}


"""my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
values_sum = sum(my_dictionary.values())

print(values_sum)
"""


#3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]


"""my_list = [1, 2, 3, 4, 5, 3, 2, 1]
new_list = list(set(my_list))
print(new_list)
"""


#3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#     - найдите значения, которые встречаются в обоих множествах
#    - найдите значения, которые не встречаются в обоих множествах
#     - проверьте являются ли эти множества подмножествами друг друга


"""set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}

common_values = set1.intersection(set2)
print(common_values)
not_common_values = set1.symmetric_difference(set2)
print(not_common_values)
print(set1.issubset(set2))
print(set2.issubset(set1))
"""






