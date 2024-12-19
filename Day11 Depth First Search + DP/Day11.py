datas = []

with open("day11.txt", "r") as file:
    datas = file.readline().strip().split()

def isZero(digit):
    return str(digit) == '0'

def isEven(digit):
    return len(str(digit)) % 2 == 0

i = 0
while i < 25:
    new_datas = []
    j = 0
    while j < len(datas):
        if isZero(datas[j]):
            new_datas.append('1')
        elif isEven(datas[j]):
            num_str = str(datas[j])
            mid = len(num_str) // 2
            left_part = num_str[:mid].lstrip('0')
            right_part = num_str[mid:].lstrip('0')
            if right_part == '':
                right_part = '0'
            if left_part == '':
                left_part = '0'
            new_datas.append(left_part)
            new_datas.append(right_part)
        else:
            new_datas.append(str(int(datas[j]) * 2024))
        j += 1
    datas = new_datas
    i += 1

print(len(datas))

## part 2

count = 0
memo = {}

def dfs(element, iter):  ## O(n)
    global count
    if iter == 75:
        count += 1
        return

    if (element, iter) in memo:
        count += memo[(element, iter)]
        return

    initial_count = count

    if isZero(element):
        dfs('1', iter + 1)  ## Worst case O(n)
    elif isEven(element):  ## Worst case O(n)
        mid = len(element) // 2
        lhs = element[:mid].lstrip('0')
        rhs = element[mid:].lstrip('0')
        if rhs == '':
            rhs = '0'
        dfs(lhs, iter + 1)  ## Worst case O(n^m) where m is depth
        dfs(rhs, iter + 1)
    else:  ## Worst case O(n)
        dfs(str(int(element) * 2024), iter + 1)

    memo[(element, iter)] = count - initial_count

## Time Complexity
## Worst Case O(n^m)

for j in range(len(datas)):  ## O(n)
    dfs(datas[j], 0)

print(count)  # Output the count
