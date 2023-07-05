import string
import keyword

name = input("Введіть рядок: ")
if not (name[0] == '_' or name[0].isalpha()):
    print(False)
    quit()
if name.isdigit():
    print(False)
    quit()
    valid_characters = string.ascii_letters + string.digits + '_'
    if any(char not in valid_characters for char in name):
        print(False)
        quit()
    if name not in keyword.kwlist:
        pass
    else:
        print(False)
        quit()
    print(True)