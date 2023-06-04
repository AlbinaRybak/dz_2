number= input ("Type 4x:")

digit1= int(number) // 1000
digit2= (int(number) // 100) % 10
digit3= (int(number) // 10) % 10
digit4= int(number) % 10

print(digit1)
print(digit2)
print(digit3)
print(digit4)