# a = [1, 3, 2, 5]
# print(a, "a")
# print(a[::-1], 'a reversed copy')

# a.reverse()
# print(a, 'a')

# print(sorted(a), 'sorted copy')

# a.sort()

# print(a, 'a')

# a.sort(reverse=True)
# print(a, 'a')

# b = a.copy()
# c = a[:]

# print(b, "b")
# print(c, "c")


# marks = ["bad", "good", 'exelent', "bad", "bad", "good"]


# def marks_order(mark: str):
#     if (mark == 'bad'):
#         return 1
#     elif (mark == "good"):
#         return 2
#     else:
#         return 3


# print(sorted(marks, key=marks_order))

# boys = ['Sasha', 'Dima']
# girls = ['Tania', 'Nastia', 'Lera']

# # boys.extend(girls)
# # print(boys)

# students = boys + girls
# print(students)

# arr = [0, 10, 100, 111, 2]

# print(min(arr))
# print(max(arr))


# def max_divided_twice(num: int):
#     if (num % 2 == 0):
#         return num
#     return -1


# print(max(arr, key=max_divided_twice))

# print(max(arr, key=lambda x: x if x % 2 == 0 else -1))

# function all() = 1 and 2 and 3 and 4
# function any() = 1 or 2 or 3 or 4


# def weekday_order(weekday: str) -> int:
#     if (weekday == "Monday"):
#         return 1
#     if (weekday == "Tuesday"):
#         return 2
#     if (weekday == "Wednesday"):
#         return 3
#     if (weekday == "Thursday"):
#         return 4
#     if (weekday == "Friday"):
#         return 5
#     if (weekday == "Saturday"):
#         return 6
#     if (weekday == "Sunday"):
#         return 7


# def sort_weekdays(weekdays: list) -> list:
#     weekdays.sort(key=weekday_order)
#     return weekdays


# print(sort_weekdays(["Saturday", "Wednesday"]))


def all_targets_hit(attempts_for_each_target: list) -> bool:
    targets_results = []
    for current_target_attempts in attempts_for_each_target:
        targets_results.append(any(current_target_attempts))
    return all(targets_results)


attempts = [
    [True, False, True],  # Постріли у першу мішень
    [False, False, True],  # Постріли у другу мішень
    [False, False],  # Постріли у третю мішень
]
attempts2 = [
    [True, False, True],  # Постріли у першу мішень
    [False, False, True],  # Постріли у другу мішень
    [False, True],  # Постріли у третю мішень
]
print(all_targets_hit(attempts))
print(all_targets_hit(attempts2))
