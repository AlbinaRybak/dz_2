num = int(input("Введіть ціле число: "))

while num >= 10:
    product = 1
    while num > 0:
        digit = num % 10
        product *= digit
        num //= 10
    num = product

print("Результат:")
