while True:
    expression = input("Введіть вираз: ")
    try:
        result = eval(expression)
        print("Результат:", result)
    except Exception as e:
        print("Помилка обчислення:", str(e))
        choice = input("Бажаєте продовжити? (y/n): ")
        if choice.lower() != "y":
            break