attendance = ["Ada", "Tunde", "Ada", "Chi", "Tunde", "Ada"]
names =[]
for each_name in attendance:
    if each_name not in names:
        names.append(each_name)
print(names)
print()

print(set(attendance))
print()

nums = [1, 2, 2, 3, 4, 4, 4, 5]
print(set(nums))
print()

# sets have .add() to put in a new item. Create an empty set with s = set(), add "a", "b", then add "a" again. Print s after each step. 
# What happens on the third add?
s = set()
s.add ('a')
print(s)
print()

s.add('b')
print(s)
s.add ('a')
print(s)
print()

print('c' not in s)
print()

s.remove('b')
print(s)
print()

s = {}
print(type(s))
print()

people = ("Ada", "Tunde", "Ada", "Chi", "Tunde", "Ada")
listed_people = list(people)
listed_people.insert(1, 'Chioma')
people = tuple(listed_people)
print(people)
print(set(people))

#write a line that checks if 25 is in big_set and prints True or False.
big_set = {10, 20, 30, 40, 50}
print(25 in big_set)