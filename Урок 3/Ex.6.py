def int_func(string):
    return string.title()


print (int_func("leonardo"))


def ext_func(phrase):
    return int_func(phrase)

print (ext_func("may the force be with you"))
