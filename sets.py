attendance = ["Ada", "Tunde", "Ada", "Chi", "Tunde", "Ada"]
names =[]
for each_name in attendance:
    if each_name not in names:
        names.append(each_name)
print(names)

names = set(attendance)
print(names)
print(set(attendance))
print()

nums = [1, 2, 2, 3, 4, 4, 4, 5]
print(set(nums))

# sets have .add() to put in a new item. Create an empty set with s = set(), add "a", "b", then add "a" again. Print s after each step. 
# What happens on the third add?
s = set()
s.add ('a')
print(s)
s.add('b')
print(s)
s.add ('a')
print(s)

