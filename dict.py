student = {"name": "Ada", "age": 22, "grades": [90, 85]}
print(student['age'])

#1
book = {"title": 'Uncle Toms Cabin', "author": 'Harriet Beecher Stowe', "pages": 412}
print(book['author'])

#2
book['pages'] = 444
print(book)

#3
book['published_year'] = 1986
print(book)

#4
#print(book['publisher'])   this will crash as no 'publisher' key

#with get(), there'll be no crash 
print(book.get('publisher'))            # will print None

print(book.get('publisher', 'Key not in dictionary'))        #yo statement will print if key dont exist

#5
print('author' in book)
print('publisher' in book)
print(444 in book)  #only check keys, never values
print()

#looping through a dict
for key, value in book.items():
    print(key, value) 
    print(value)
print()
#looping through just keys
for key in book.keys():
    print(key)
print()
#through just values
for value in book.values():
    print(value, '\n')
print(book.keys())
print(list(book.keys()))
print(book.values())
print()

joy, job = book.keys(), book.values()
print(job)
print(joy)
print(list(joy))
print(type(job))
print(type(joy))
print('grade' not in student)
print()


# COpying a dict makes a new dict
original = {"name": "Ada", "tags": ["python"]}
copy1 = original.copy() #shallow copy leaks through shared list - modify 2nd list will affect original
print(copy1)

original['name'] = 'Ade'    #replacing(not appending) never affects the 2nd dict
copy1['name'] = 'Joy'
print(original)
print(copy1)
print()

copy1['tags'].append('rust')   #modify the list here changes orininal too
copy1['tags'][0] = 'go'
print(copy1)
print(original)
print()

#deep copying so list in original becomes independent
info = {"club": "Betis", "player(s)": ["Isco"]}
copy2 = info.copy()
copy2['player(s)'] = info['player(s)'].copy()    #if info had 2 keys with list as values, you copy both lists separately
copy2['player(s)'].append('Antony')
print(info['player(s)'])
print(copy2['player(s)'])
print(info)
print(copy2)
print(info['club'] is copy2['club'])
print(info['player(s)'] is not copy2['player(s)'])
print()
#for large dicts, use inbuilt function to deepcopy
pro ={'city': 'London', 'teams': ['Chelsea', 'Arsenal'], 'competitions': ['UCL', 'PL']}

import copy
quo = copy.deepcopy(pro)
quo['teams'].append('West Ham')
print(pro)
print(quo)
print()

#nested dict
student = {
    "name": "Ada",
    "age": 22,
    "grades": [90, 85, 95],
    "address": {
        "city": "Lagos",
        "state": "Lagos State"
    }
}
print(student)
print()

student['address']['city'] = 'Chicago'
student['address']['state'] = 'Illinois'
student['name'] = 'King Von'
student['address']['apartment'] = 'O Block'
print(student)

print(student['address'].get('apartment'))  #get() works same way
print(student['address'].get('aparte', 'Dont exist! X'))

print(student.pop('grades'))   #pop() - same work 
print(student)
print(student['address'].pop('class', 'No such key'))
print()

#to rename a key, pop it into new value of key
student['bodies'] = student.pop('age')
print(student)
print()

#Asserting that an error gets raissed
def check_positive(n):
    if n < 0:         #if bug so > 0, so it dont flag -ve nums, then assert str will read
        raise ValueError("must be positive")
    return n
print(check_positive(-2))    #if error raised, no need to check try
                            #if return n
# Write a test using the try/except/assert False pattern,
#  proving that check_positive(-5) raises ValueError.
try:
    check_positive(-2)
    assert False, 'ValueError expected but not raised'
except ValueError:
    pass   #confirms error is caught, no action needed. you can rejected +=1 (increase a counter, etc)
