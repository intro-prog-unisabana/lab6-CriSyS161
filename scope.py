int_value = 10
str_value = "Hello"
def set_globals(some_int, some_str):
    x = int()
    y = ("")

def get_globals():
    if int_value:
        print(int_value)
    else:
        print(None)
    if str_value:
        print(str_value)
    else:
        print(None)

print(get_globals())       # Salida: (None, None)
set_globals(10, "Hello")
print(get_globals())       # Salida: (10, "Hello")