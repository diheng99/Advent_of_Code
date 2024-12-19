datas = []

with open("day12.txt", "r") as file:
    for line in file:
        datas.append(list(line.strip()))

visited = [[False for _ in range(len(datas[0]))] for _ in range(len(datas))]
perimeter = 0

def outOfRange(row, col):
    if row < 0 or row >= len(datas):
        return True
    if col < 0 or col >= len(datas[0]):
        return True
    return False

def findAdjacentTop(row, col, curElement):
    newRow = row - 1
    newCol = col

    if not outOfRange(newRow, newCol):
        if datas[newRow][newCol] == curElement:
            return 0
    return 1

def appendTop(val, stack, row, col):
    global perimeter
    newRow = row - 1
    newCol = col
    if outOfRange(newRow, newCol):
        perimeter += 1
        return
    if datas[newRow][newCol] == val and not visited[newRow][newCol]:
        visited[newRow][newCol] = True
        stack.append([datas[newRow][newCol], newRow, newCol])
    if datas[newRow][newCol] != val:
        perimeter += 1

def appendBot(val, stack, row, col):
    global perimeter
    newRow = row + 1
    newCol = col
    if outOfRange(newRow, newCol):
        perimeter += 1
        return
    if datas[newRow][newCol] == val and not visited[newRow][newCol]:
        visited[newRow][newCol] = True
        stack.append([datas[newRow][newCol], newRow, newCol])
    if datas[newRow][newCol] != val:
        perimeter += 1

def appendLeft(val, stack, row, col):
    global perimeter
    newRow = row
    newCol = col - 1
    if outOfRange(newRow, newCol):
        perimeter += 1
        return
    if datas[newRow][newCol] == val and not visited[newRow][newCol]:
        visited[newRow][newCol] = True
        stack.append([datas[newRow][newCol], newRow, newCol])
    if datas[newRow][newCol] != val:
        perimeter += 1

def appendRight(val, stack, row, col):
    global perimeter
    newRow = row
    newCol = col + 1
    if outOfRange(newRow, newCol):
        perimeter += 1
        return
    if datas[newRow][newCol] == val and not visited[newRow][newCol]:
        visited[newRow][newCol] = True
        stack.append([datas[newRow][newCol], newRow, newCol])
    if datas[newRow][newCol] != val:
        perimeter += 1

result = 0

for row in range(len(datas)):
    for col in range(len(datas[0])):
        if visited[row][col]:
            continue
        curElement = datas[row][col]
        stack = []
        stack.append([curElement, row, col])
        visited[row][col] = True
        count = 0
        perimeter = 0
        while stack:
            item = stack.pop()
            count += 1
            curVal = item[0]
            curRow = item[1]
            curCol = item[2]
            appendTop(curVal, stack, curRow, curCol)
            appendBot(curVal, stack, curRow, curCol)
            appendRight(curVal, stack, curRow, curCol)
            appendLeft(curVal, stack, curRow, curCol)
        result += (perimeter * count)

print(result)

########################### PART 2 ###########################

# day12.py

visited = [[False for _ in range(len(datas[0]))] for _ in range(len(datas))]
perimeter = 0

def outOfRange(row, col):
    if row < 0 or row >= len(datas):
        return True
    if col < 0 or col >= len(datas[0]):
        return True
    return False

def findAdjacentTop(row, col, curElement):
    newRow = row - 1
    newCol = col
    if not outOfRange(newRow, newCol):
        if datas[newRow][newCol] == curElement:
            return 1
    return 0

def appendTop(val, stack, row, col):
    global perimeter
    newRow = row - 1
    newCol = col
    if outOfRange(newRow, newCol):
        perimeter += 1
        return
    if datas[newRow][newCol] == val and not visited[newRow][newCol]:
        visited[newRow][newCol] = True
        visited2[newRow][newCol] = True
        stack.append([datas[newRow][newCol], newRow, newCol])
    if datas[newRow][newCol] != val:
        perimeter += 1

def appendLeft(val, stack, row, col):
    global perimeter
    newRow = row
    newCol = col - 1
    if outOfRange(newRow, newCol):
        perimeter += 1
        return
    if datas[newRow][newCol] == val and not visited[newRow][newCol]:
        visited[newRow][newCol] = True
        visited2[newRow][newCol] = True
        stack.append([datas[newRow][newCol], newRow, newCol])
    if datas[newRow][newCol] != val:
        perimeter += 1

def appendRight(val, stack, row, col):
    global perimeter
    newRow = row
    newCol = col + 1
    if outOfRange(newRow, newCol):
        perimeter += 1
        return
    if datas[newRow][newCol] == val and not visited[newRow][newCol]:
        visited[newRow][newCol] = True
        visited2[newRow][newCol] = True
        stack.append([datas[newRow][newCol], newRow, newCol])
    if datas[newRow][newCol] != val:
        perimeter += 1

for row in range(len(datas)):
    for col in range(len(datas[0])):
        visited2 = [[False for _ in range(len(datas[0]))] for _ in range(len(datas))]
        if visited[row][col]:
            continue
        curElement = datas[row][col]
        stack = []
        stack.append([curElement, row, col])
        visited[row][col] = True
        visited2[row][col] = True
        count = 0
        perimeter = 0
        while stack:
            item = stack.pop()
            count += 1
            curVal = item[0]
            curRow = item[1]
            curCol = item[2]
            appendTop(curVal, stack, curRow, curCol)
            appendLeft(curVal, stack, curRow, curCol)
            appendRight(curVal, stack, curRow, curCol)

print(result)
