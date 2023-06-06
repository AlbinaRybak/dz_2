input_list = [7,8,9,10]
output_list= []

if len(input_list) >1:
    last_element = input_list.pop()
    input_list.insert(0,last_element)
    output_list = input_list
else:
    output_list = input_list

print(output_list)