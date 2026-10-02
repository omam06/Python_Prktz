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
print()

#3
member1_books = {'book1', 'book2', 'book3', 'book4', 'book5', 'book6'}
member2_books = {'book5', 'book8', 'book3', 'book9', 'book10', 'book12', 'book6'}
member1_books.add('book21')             #append
member1_books.remove('book4')
member2_books.update({'book13', 'book14', 'book17'})   #extend in lists
print(member1_books)
print(member2_books)
print(member1_books ^ member2_books)  #opposite of intersection& - combination w/o common items
print()
#Write a function safe_remove(book_set, book) that removes book from book_set if it's there, 
# and does nothing (no crash) if it isn't. 
# Test it once with a book that exists in the set, and once with a book that doesn't.
def safe_remove(book_set, book):
    book_set.discard(book)
    print(book_set)
safe_remove(member1_books, 'book5')
safe_remove(member2_books, 'book44')