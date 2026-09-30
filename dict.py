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
print(book.get('publisher'))

print(book.get('publisher', 'Key not in dictionary'))

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
print(book.values())
print()

joy, job = book.keys(), book.values()
print(job)
print(joy)
print(list(joy))
print(type(job))
print(type(joy))
print()

#copy()

