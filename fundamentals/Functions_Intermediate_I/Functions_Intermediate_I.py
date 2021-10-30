# 1 Update Values in Dictionaries and Lists
x = [[5, 2, 3], [10, 8, 9]]
print(x)
x[1][0] = 15  # Updating the value in a list
print(x)

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
# changing a key's value in a list of dictionaries
(students[0]['last_name']) = 'Bryant'
print(students)


sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']


}
# changing a specfic value in list of values of a dictionary
(sports_directory['soccer'][0]) = 'Andres'
print(sports_directory)
z = [{'x': 10, 'y': 20}]
(z[0]['y']) = 30
print(z)

# 2 Iterate Through a List of Dictionaries
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(students):
    print((students[0]))
    print((students[1]))
    print((students[2]))
    print((students[3]))


(iterateDictionary(students))

# 3 Get Values From a List of Dictionaries


students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'},
]


def iterateDictionary2(key_name, some_list):

    print(some_list[0][key_name])
    print(some_list[1][key_name])
    print(some_list[2][key_name])
    print(some_list[3][key_name])


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# 4 Iterate Through a Dictionary with List Values


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    print(len(dojo['locations']), 'LOCATIONS')
    for x in range(0, len(dojo['locations'])):
        print(dojo['locations'][x])
    print('-------')
    print(len(dojo['instructors']), 'INSTRUCTORS')
    for x in range(0, len(dojo['instructors'])):
        print(dojo['instructors'][x])


printInfo(dojo)
