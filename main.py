#Практическое задание 1
my_dict = {'Andrey': 1986, 'Elena': 1992, 'Sergey': 2008}
print(my_dict)
print(my_dict['Elena'])
my_dict['Nastya'] = 2011
my_dict.update({'Alex': 2018,
                'Angel': 2025})
del my_dict['Sergey']
print(my_dict.get('Sergey'))
print(my_dict.get('Sergey', 2008))
print(my_dict)

#Практическое задание 2
my_set = {'a', 'b', 1, 2, 3, 'a', 2}
print(my_set)
print(my_set.update('d', [(1, 2)]))
print(my_set.remove('b'))
print(my_set)
