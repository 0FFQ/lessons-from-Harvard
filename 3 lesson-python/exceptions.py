import sys
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("нельзя ввести подобный символ")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("нельзя делить на 0")
    sys.exit(1)


print(f"{x} / {y} = {result}")