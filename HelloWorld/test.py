user_input = input("Please enter 3 numbers separated by commas: ")
numbers = user_input.split(sep=",")
for index in range(len(numbers)):
    numbers[index] = int(numbers[index])
answer = numbers[0] + numbers[1] - numbers[2]
print(answer)