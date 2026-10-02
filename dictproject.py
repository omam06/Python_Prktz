student = {'name': 'Takeoff', 'age': 28, 'grades': [65, 765, 786], 'address': {'city': 'Georgia', 'state': 'Atlanta'}}
def update_grade(student, new_grade):
    student['grades'].append(new_grade)
    return student
print(update_grade(student, 419))

def get_city(student):
    return student['address'].get('city', 'Unknown')
print(get_city(student))
print()

print(student['address'].pop('state'))
def average_grade(student):
    return sum(student['grades']) / len('grades')
print(average_grade(student))
