import string
import keyword

def is_valid_variable_name(name):
    import string
    import keyword

    def is_valid_variable_name(name):
        if name.isdigit():
            return False
        valid_characters = string.ascii_letters + string.digits + '_'
        if any(char not in valid_characters for char in name):
            return False
        if name in keyword.kwlist:
            return False
        return True

    variable_names = [
        "_",
        "x",
        "get_value",
        "get value",
        "get!value",
        "some_super_puper_value",
        "Get_value",
        "get_Value",
        "getValue",
        "3m",
        "m3" ]

    for name in variable_names:
        print(name, "=>", is_valid_variable_name(name))