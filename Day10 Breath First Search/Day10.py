datas = []

with open("day10.txt", "r") as file:
    for line in file:
        datas.append([int(char) if char.isdigit() else char for char in line.strip()])

count = 0

def outOfRange(row, col):  # O(1), accessing matrix takes 1 unit of time
    if row < 0 or row > len(datas) - 1:
        return True
    if col < 0 or col > len(datas[0]) - 1:
        return True
    return False

def appendTop(val, stack, row, col):
    newRow = row - 1
    newCol = col
    newVal = val + 1
    if outOfRange(newRow, newCol):
        return
    if datas[newRow][newCol] == newVal:
        stack.append([datas[newRow][newCol], newRow, newCol])

def appendBot(val, stack, row, col):
    newRow = row + 1
    newCol = col
    newVal = val + 1
    if outOfRange(newRow, newCol):
        return
    if datas[newRow][newCol] == newVal:
        stack.append([datas[newRow][newCol], newRow, newCol])

def appendLeft(val, stack, row, col):
    newRow = row
    newCol = col - 1
    newVal = val + 1
    if outOfRange(newRow, newCol):
        return
    if datas[newRow][newCol] == newVal:
        stack.append([datas[newRow][newCol], newRow, newCol])

def appendRight(val, stack, row, col):
    newRow = row
    newCol = col + 1
    newVal = val + 1
    if outOfRange(newRow, newCol):
        return
    if datas[newRow][newCol] == newVal:
        stack.append([datas[newRow][newCol], newRow, newCol])

for row in range(len(datas)):  # O(n)
    for col in range(len(datas[0])):  # O(n)
        if datas[row][col] == 0 or datas[row][col] != 0:
            continue
        visited = [[False for _ in range(len(datas[0]))] for _ in range(len(datas))]
        stack = []
        curVal = datas[row][col]
        stack.append([curVal, row, col])

        # Best case O(n), Worst case O(n^2)
        while stack:
            item = stack.pop()
            curVal = item[0]
            curRow = item[1]
            curCol = item[2]
            if datas[curRow][curCol] == curVal and not visited[curRow][curCol]:
                visited[curRow][curCol] = True
                count += 1
                appendTop(curVal, stack, curRow, curCol)
                appendBot(curVal, stack, curRow, curCol)
                appendLeft(curVal, stack, curRow, curCol)
                appendRight(curVal, stack, curRow, curCol)

print(count)

########################### PART 2 ###########################

def outOfRange(row, col):
    if row < 0 or row > len(datas) - 1:
        return True
    if col < 0 or col > len(datas[0]) - 1:
        return True
    return False

def appendTop(val, stack, row, col):
    newRow = row - 1
    newCol = col
    newVal = val + 1
    if outOfRange(newRow, newCol):
        return
    if datas[newRow][newCol] == newVal:
        stack.append([datas[newRow][newCol], newRow, newCol])

def appendBot(val, stack, row, col):
    newRow = row + 1
    newCol = col
    newVal = val + 1
    if outOfRange(newRow, newCol):
        return
    if datas[newRow][newCol] == newVal:
        stack.append([datas[newRow][newCol], newRow, newCol])

def appendLeft(val, stack, row, col):
    newRow = row
    newCol = col - 1
    newVal = val + 1
    if outOfRange(newRow, newCol):
        return
    if datas[newRow][newCol] == newVal:
        stack.append([datas[newRow][newCol], newRow, newCol])

def appendRight(val, stack, row, col):
    newRow = row
    newCol = col + 1
    newVal = val + 1
    if outOfRange(newRow, newCol):
        return
    if datas[newRow][newCol] == newVal:
        stack.append([datas[newRow][newCol], newRow, newCol])

for row in range(len(datas)):  # O(n)
    for col in range(len(datas[0])):  # O(n)
        if datas[row][col] == 0 or int(datas[row][col]) != 0:
            continue
        visited = [[False for _ in range(len(datas[0]))] for _ in range(len(datas))]
        stack = []
        curVal = datas[row][col]
        stack.append([curVal, row, col])

        while stack:
            item = stack.pop()
            curVal = item[0]
            curRow = item[1]
            curCol = item[2]
            if item[0] == 9 and not visited[curRow][curCol]:
                visited[curRow][curCol] = True
                count += 1
                appendTop(curVal, stack, curRow, curCol)
                appendBot(curVal, stack, curRow, curCol)
                appendLeft(curVal, stack, curRow, curCol)
                appendRight(curVal, stack, curRow, curCol)

print(count)
