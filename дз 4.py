operation = input("Введіть операцію (+, -, *, /): ")
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Помилка: Дільник не може бути нулем!")
        result = None
else:
    print("Помилка: Невідома операція!")
    result = None

if result is not None:
    print("Результат:", result)