# 2.Составить генератор (yield), который переведет символы строки из нижнего
# регистра в верхний.
def uppercase_generator(input_string):
    for char in input_string:
        if char.islower():
            yield char.upper()
        else:
            yield char

input_string = "Hello, World!"
result = ''.join(uppercase_generator(input_string))
print(result)
