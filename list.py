numbers = [10,12,14]

print(numbers)
print(numbers[2])
print(len(numbers))

numbers.append(100)
numbers[1] = 11

numbers.insert(2,12)
numbers.insert(3,13)

numbers.pop()

print(numbers)


arr = [0,0,0]
arr2 = [0] * 100

print(arr)
print(arr2)


arr3 = [1,2,3,4,5]
print(3 in arr3)
print(arr3.index(3))
print(arr3[2:4])