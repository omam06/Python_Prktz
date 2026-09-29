attendance = ["Ada", "Tunde", "Ada", "Chi", "Tunde", "Ada"]
names =[]
for each_name in attendance:
    if each_name not in names:
        names.append(each_name)
print(names)

names = set(attendance)
print(names)
print(set(attendance))