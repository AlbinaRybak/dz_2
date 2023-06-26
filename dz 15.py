num = int(input("Введіть кількість секунд: "))

if num < 0 or num >= 8640000:
    print("Неприпустиме значення!")
else:
    days, remainder = divmod(num, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    day_str = "день" if days == 1 else "днів"
    time_str = f"{days} {day_str}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
    print("Результат:", time_str)