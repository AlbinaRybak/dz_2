my_list = [1, 0, 2, 0, 3, 0, 4, 5, 0]

zeros_count = my_list.count(0)
index = 0

while zeros_count > 0:
    if my_list[index] == 0:
        my_list.pop(index)
        my_list.append(0)
        zeros_count -= 1
    else:
        index += 1

print(my_list)