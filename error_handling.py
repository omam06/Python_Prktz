# error handling is using try/except to catch and respond to specific exception types that might occur, so your program can recover gracefully instead of crashing entirely. Python lets you catch multiple different exception types in the same try block, each with its own except, handling each one differently if needed.
#1
def safe_divide(tinubu):
    try:
        echo = int(tinubu)
        math = 100 / echo
    except ValueError:
        return "echo must be a valid integer"
    except ZeroDivisionError:
        return "canNOT divide by zero"       #else only run if try succeeds. finally run no matter what
    else:
        return f"Converted successfully: {echo}"
        return mth
   
print(safe_divide("abc"))
print(safe_divide("0"))
print(safe_divide("4"))

print()

#2
def check(text):
    try:
        n = int(text)
    except (ValueError, TypeError):  #same msg 4 both. else, separately.
        print("bad")
    else:
        print("ok", n)
    finally:
        print("done")

check("5")
check(None)
check('jhcv')
print()


def safe_to_int(value):
    try:
        sharp = int(value)
        return sharp
    except (ValueError, TypeError):
        return None

print(safe_to_int("5"))
print(safe_to_int("x"))
print(safe_to_int(None))
print(safe_to_int("3.5"))

print()


#keeps asking till user enter  num>0
def ask_positive_number():
    while True:
        try:
            ent = int(input("enter number: "))
            if ent > 0:
                return ent
            else:
                print("Number must be above 0")
        except ValueError:
            print("You did not enter a valid number. Try again")
print(ask_positive_number())
