number=int(input("Typr 5x:"))
reversed_number = 0
reversed_number += (number % 10) * 10000
number //= 10
reversed_number+= (number % 10) * 1000
number //= 10
reversed_number+=(number % 10 ) * 100
number //= 10
reversed_number+=(number % 10) * 10
number //= 10
reversed_number+=number
print(reversed_number)