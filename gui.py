def make_multiplier(x):
    def multiply(y):
        return x * y
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))
print(triple(5))
python_course = {'Metro', '21 Savage', 'Wunna', 'Weezy', 'Quavo'}
web_course = {'Drizzy', 'Weezy', 'Breezy', 'YG', 'Wunna'}
print(python_course ^ web_course)
print(python_course - web_course)