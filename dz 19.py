def common_elements():
    multiples_of_3 = [num for num in range(3, 100) if num % 3 == 0]
    multiples_of_5 = [num for num in range(5, 100) if num % 5 == 0]
    return set(multiples_of_3) & set(multiples_of_5)

common_elements()