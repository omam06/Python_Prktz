day1 = {'Jane', 'John', 'James', 'Gabriel', 'Joy'}
day2 = {'Gabriel', 'Keith', 'Jane', 'Von', 'Damian'}
students_who_came_atlest_once = day1 | day2
print(students_who_came_atlest_once)

students_who_attended_both_days = day1 & day2
print(students_who_attended_both_days)

students_who_attended_day1_only = day1 - day2
print(students_who_attended_day1_only)

#Write a function check_attendance(students, name) that takes a set and a name, and returns True or False depending on whether that name is in the set.
#Test it on both day1 and day2 with a name you know is in one but not the other.
def check_attendance(students, name):
    return name in students

print(check_attendance(day1, 'James'))
print(check_attendance(day2, 'John'))
print()

#2
python_course = {'Metro', '21 Savage', 'Wunna', 'Weezy', 'Quavo'}
web_course = {'Drizzy', 'Weezy', 'Breezy', 'YG', 'Wunna'}
print(python_course | web_course)
print(python_course & web_course)
print(web_course - python_course)
python_course.add('Roddy')
print(python_course)
#Write a function total_unique_students(set1, set2) that returns the count of students 
# across both courses combined, with no one counted twice.
def total_unique_students(set1, set2):
    return len(set1 | set2)
print(total_unique_students(python_course, web_course))