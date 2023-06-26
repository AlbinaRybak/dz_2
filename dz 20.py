def add_one(some_list):
    number = int(''.join(map(str, some_list)))
    number += 1
    result = [int(digit) for digit in str(number)]
    return result
print(add_one([1, 2, 3, 4]))
print(add_one([9, 9, 9]))
print(add_one([0]))
print(add_one([9]))          
