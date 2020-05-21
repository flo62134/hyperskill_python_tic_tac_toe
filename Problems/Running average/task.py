def get_running_average(number1: int, number2: int):
    return (number1 + number2) / 2


list = [int(number) for number in list(input())]
averages = [get_running_average(list[index - 1], list[index]) for index in range(1, len(list))]
print(averages)
