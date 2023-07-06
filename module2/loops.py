# for i in range(3):
#     print(i)

# for i in range(0, 3, 1):
#     print(i)

# # Won't work
# for i in range(0, 3, -1):
#     print(i)


# index = 0

# while True:
#     index += 1
#     print(index)
#     print("OK")
#     if (index >= 3):
#         break

# for i in range(10):
#     if (i % 2 != 0):
#         continue

#     print(i)
#     print("OK")

# nums = [3, 5, 7]
# for num in nums:
#     print(num)

# print("Num after loop", num)

arr = [41, 22, 53, 80, 12, 16]


def is_second_digit_bigger(numbers: list[int]) -> list[bool]:
    prev_numbers = []
    result = []
    for i in numbers:
        last_number = str(i)[-1:]
        last_number = int(last_number)
        curr_result = True

        for j in prev_numbers:
            if last_number > j:
                curr_result = True
            else:
                curr_result = False
                break

        prev_numbers.append(last_number)
        result.append(curr_result)
    return result


def is_second_digit_bigger2(numbers: list[int]) -> list[bool]:
    result = []
    for i in range(len(numbers)):
        current_second_digit = numbers[i] % 10
        is_greater = True

        for j in (range(i)):
            temp_second_digit = numbers[j] % 10

            if temp_second_digit > current_second_digit:
                is_greater = False
        result.append(is_greater)
    return result


print(is_second_digit_bigger(arr))
print(is_second_digit_bigger2(arr))


# def get_years(amount: int, percent: int, limit: int) -> int:
#     temp_amount = amount
#     years = 0
#     while temp_amount <= limit:
#         temp_amount += temp_amount * (percent / 100)
#         years += 1
#     return years - 1


# get_years(1000, 10, 1100)


# def check_is_prime(number: int) -> bool:
#     number = abs(number)
#     res = True
#     if (number == 0 or number == 1):
#         res = False
#     for i in range(2, number):
#         if (number % i == 0):
#             res = False

#     return res


# print(check_is_prime(-47))
