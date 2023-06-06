number1 = float(input("Введіть перше число: "))
operation = input("Введіть дію (+, -, *, /): ")
number2 = float(input("Введіть друге число: "))

if operation == '+':
    result = number1 + number2
    print("Результат:", result)
elif operation == '-':
    result = number1 - number2
    print("Результат:", result)
elif operation == '*':
    result = number1 * number2
    print("Результат:", result)
elif operation == '/':
    if number2 == 0:
        print("Помилка: Ділення на нуль неможливе!")
    else:
        result = number1 / number2
        print("Результат:", result)
else:
    print("Помилка: Невідома дія")
