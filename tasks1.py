def is_jumping(number: int) -> str:
    line = str(number)
    result = 'JUMPING'

    for i in range(1,len(line)):
        diff = int(line[i]) - int(line[i-1])
        if(abs(diff) != 1):
            result = "NOT JUMPING"
            
    return result

print(is_jumping(123456))
print(is_jumping(1223))
print(is_jumping(121))
print(is_jumping(9))


def is_special_number(number: int) -> str:
    while number > 0:
        if number % 10 > 5:
            return "NOT!!"
        number //= 10
    return "Special!!"

print(is_special_number(98))
print(is_special_number(134))