seconds = int(input("Введіть кількість секунд: "))

days = seconds // (24 * 60 * 60)
hours = (seconds // (60 * 60)) % 24
minutes = (seconds // 60) % 60
seconds = seconds % 60

if days == 1:
    days_string = "день"
else:
    days_string = "днів"

time_string = f"{days} {days_string}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
print(time_string)