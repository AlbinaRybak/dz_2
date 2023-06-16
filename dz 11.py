import string

letters = input("Введіть дві літери через дефіс: ")
min_letter, max_letter = letters.split("-")

all_letters = string.ascii_letters
start_index = all_letters.index(min_letter)
end_index = all_letters.index(max_letter)
result = all_letters[start_index : end_index + 1]

print(result)


