data = []

with open("day6.txt", "r") as file:
    for line in file:
        line = line.strip()
        data.append(list(line))

num_rows = len(data)
num_cols = len(data[0]) if num_rows > 0 else 0
matrix = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

def find_guard(data):
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char == "^":
                return (i, j)

init_posX, init_posY = find_guard(data)

def goTop(x, y):
    while x >= 0 and data[x][y] != "#":
        matrix[x][y] = 1
        x -= 1
        if x < 0:
            return
        if data[x][y] == "#":
            goRight(x + 1, y)

def goRight(x, y):
    while y < len(data[0]) and data[x][y] != "#":
        matrix[x][y] = 1
        y += 1
        if y > len(data[0]) - 1:
            return
        if data[x][y] == "#":
            goDown(x, y - 1)

def goDown(x, y):
    while x < len(data) and data[x][y] != "#":
        matrix[x][y] = 1
        x += 1
        if x > len(data) - 1:
            return
        if data[x][y] == "#":
            goLeft(x - 1, y)

def goLeft(x, y):
    while y >= 0 and data[x][y] != "#":
        matrix[x][y] = 1
        y -= 1
        if y < 0:
            return
        if data[x][y] == "#":
            goTop(x, y + 1)

def start_walk(x, y):
    goTop(x, y)

start_walk(init_posX, init_posY)

count_ones = sum(row.count(1) for row in matrix)
print("Total number of 1s:", count_ones)
