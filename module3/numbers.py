import random
x1 = 42

x2 = 0b101010
x3 = 0o52
x4 = 0X2A
x5 = 0x2a

print(x1, x2, x3, x4, x5)

print(int(0b1010))

print(2.32 % 2)


def generate_random_list(min_value: int, max_value: int, length: int) -> list:
    res = []
    for i in range(length):
        number = random.random() * max_value + min_value
        res.append(int(number))
    print(len(res))
    return res


print(generate_random_list(4, 100, 100))
