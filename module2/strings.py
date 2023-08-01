# name = "Sasha"
# message = f"Hello, {name}"

# code = ord("A")
# code2 = ord("a")

# print(chr(66))
# print(code)
# print(code2)


# print(" Print special symbol = \" ha ha")

# print(message)


# name = 'Dania'
# name2 = 'John'

# print(name.lower() < name2.lower())


# line = "   Line line    Line  line"

# print(line.strip())

# text = 'sasha zhenia sasha tolia petro'
# print(text.count("sasha"))
# print(text.count("petro"))

# students = ['Sasha', 'Masha', 'Dasha', 'Yulia']
# students_line = "".join(students)

# print(" ,, too ,, ".join(students))

# students2 = 'Sasha, Masha, Dasha'
# print(students2.split(", "))

# card_number = "5375 4435 5634 3628"

# last4 = card_number[-4:]

# card_number = "**** " * 3 + last4

# print(card_number)
# \
# phrase = "what do you like?"

# print(phrase.replace(" ", "-"))


# multiline_string = """Multiline
#        string
#                 and
#                     Sasha
# """

# print(multiline_string)


# def is_alphabet(letters: str) -> bool:
#     arr = list(letters)
#     print(arr)
#     print(len(arr))
#     res = True

#     for i in range(1, len(arr)):
#         print('in loop')
#         curr = arr[i].lower()
#         prev = arr[i - 1].lower()
#         print(ord(curr.lower()) - ord(prev.lower()))
#         if (ord(curr.lower()) - ord(prev.lower()) > 1):
#             print(ord(curr.lower()) - ord(prev.lower()))
#             res = False
#     return res


# print(is_alphabet('abcd'))


# def make_variable_name(words: str, number_of_words: int) -> str:
#     return "_".join(words.split(" ")[:number_of_words])


# print(make_variable_name("my favorite variable name is x", 3))


# def make_upper(text: str, letter: str) -> list:
#     letter_count = text.count(letter)
#     modified_text = text.replace(letter, letter.upper())
#     return [modified_text, letter_count]


# print(make_upper("aaabbabba", "b"))


# def calculate_guests(guests_input: str) -> int:
#     number = ""
#     for char in guests_input:
#         if (char.isdigit()):
#             number += char
#     print(number)


# calculate_guests("Big company of 15 dudes")

# str = "Hello, 9.75 people"
# res = []
# print(str.split())
# for num in str.split():
#     if (num.isnumeric()):
#         res.append(num)

# print(res)


# def calculate_guests(guests_input: str) -> int:
#     number = ""
#     is_decimal = False

#     for char in guests_input:
#         if (char.isdigit()):
#             number += char
#         elif char == "." and not is_decimal:
#             is_decimal = True
#             number += char
#         else:
#             if (number):
#                 break
#             is_decimal = False

#     return int(float(number)) if number and number != "0" else "not a number"


# print(calculate_guests("I think 5 guests"))
# print(calculate_guests("Hello, 9.75 people"))
# print(calculate_guests("There will be 7 or 9 guys"))


# def calculate_guests2(guests_input: str) -> int:
#     number_str = ""
#     for char in guests_input:
#         if char.isnumeric():
#             number_str += char
#         elif len(number_str) != 0:
#             break
#     return (
#         int(number_str)
#         if len(number_str) > 0 and int(number_str) != 0
#         else "not a number"
#     )


# def hello_dear_man(a: int = 0, b: int = 0, *args, **kwargs):
#     print('args', args)
#     print("kwargs", kwargs)

#     print(a+b)


# hello_dear_man()
# hello_dear_man(2, 3)
# hello_dear_man(2, 3, 4, 5, num=999)

# def print_message(username: str, message: str) -> str:
#     return f"""
#         Message from {username}:
#         {message}
#     """


# print(print_message("ad", 'heeey'))
