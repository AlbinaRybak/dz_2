import random
my_list=[]

for i in range (random.randint (6, 15)):
    my_list.append(random.randint(1,100))
print(my_list)

summa= 0
for elements in my_list:
    summa += elements
print(summa)
