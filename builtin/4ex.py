import time
import math

def square_root_after_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return math.sqrt(number)

number = 25100
milliseconds = 2123
result = square_root_after_milliseconds(number, milliseconds)
print(f"Square root of {number} after {milliseconds} milliseconds is {result}")


import time
import math

n = int(input("Sample input:\n"))
t = int(input())
time.sleep(t/1000)
result = math.sqrt(n)
print(f"Square root of {n} after {t} milliseconds is {result}")