datas = []
datagg = []

with open("day7.txt", "r") as file:
    for line in file:
        datagg.append(line)
        datas.append(line.strip().split(":"))

def recursive(prevVal, val, arr, op):
    if len(arr) == 0:
        return
    summ = arr[0]

    if op == 1:  # "+"
        summ = prevVal + arr[0]
        if summ == val:
            return True

    if op == 0:  # "*"
        summ = prevVal * arr[0]
        if summ == val:
            return True

    if recursive(summ, val, arr[1:], 1):
        return True

    if recursive(summ, val, arr[1:], 0):
        return True

def recursive2(target, curSum, arr):
    if curSum == target:
        return True
    if len(arr) == 0:
        return False

    if recursive2(target, curSum + int(arr[0]), arr[1:]):
        return True

    if recursive2(target, curSum * int(arr[0]), arr[1:]):
        return True

    return False

total = 0

for entry in datas:
    target = int(entry[0])
    numbers = list(map(int, entry[1].strip().split()))
    if recursive2(target, numbers[0], numbers[1:]):
        total += target

print(total)  # Example output: 5512534574980

def part2(data):
    equations = []
    for line in data:
        test_value, numbers = line.split(":")
        equations.append((int(test_value), list(map(int, numbers.strip().split()))))

    result = []
    for test_value, numbers in equations:
        possibles = [numbers.pop(0)]
        while numbers:
            curr = numbers.pop(0)
            temp = []
            for p in possibles:
                next_values = [
                    p + curr,
                    p * curr,
                    int(str(p) + str(curr))
                ]
                temp.extend([v for v in next_values if v <= test_value])
            possibles = temp
        if test_value in possibles:
            result.append(test_value)

    return sum(result)

x = part2(datagg)
print(x)
