# error handling is using try/except to catch and respond to specific exception types that might occur, so your program can recover gracefully instead of crashing entirely. Python lets you catch multiple different exception types in the same try block, each with its own except, handling each one differently if needed.
#pr1
def safe_divide(num_str):
    try:
        echo = int(num_str)
        math = 100 / echo
    except ValueError:
        return "echo must be a valid integer"
    except ZeroDivisionError:
        return "canNOT divide by zero"       #else only run if try succeeds. finally run no matter what
    else:
        return "Converted successfully:", echo
        return mth
   
print(safe_divide("abc"))
print(safe_divide("0"))
print(safe_divide("4"))

