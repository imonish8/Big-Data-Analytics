def char_frequency_simple(input_string):
    for char in set(input_string):
        print(f"'{char}': {input_string.count(char)}")

input_string = "Hello World"
char_frequency_simple(input_string)