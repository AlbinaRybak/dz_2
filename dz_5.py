input_list = [1, 2, 3, 4, 5, 6]
output_list = []

if len(input_list) == 0:
    output_list.append([])
    output_list.append([])
elif len(input_list) % 2 == 0:
    middle = len(input_list) // 2
    output_list.append(input_list[:middle])
    output_list.append(input_list[middle:])
else:
    middle = len(input_list) // 2 + 1
    output_list.append(input_list[:middle])
    output_list.append(input_list[middle:])

print(output_list)
