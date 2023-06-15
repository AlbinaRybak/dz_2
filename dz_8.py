input_array = [0, 1, 7, 2, 4, 8]

result = 0
if len(input_array) > 0:
    sum_of_even_index_elements = 0
    for i in range(0, len(input_array), 2):
        sum_of_even_index_elements += input_array[i]
    last_element = input_array[-1]
    result = sum_of_even_index_elements * last_element

print(result)
