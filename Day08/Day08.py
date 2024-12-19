datas = []

with open("day8.txt", "r") as file:
    for line in file:
        datas.append(line.strip())  # Strip and append each line

res = 0
rowSize, colSize = len(datas) - 1, len(datas[0]) - 1
visited = [[False for _ in range(colSize + 1)] for _ in range(rowSize + 1)]
count = 0

def markAntinode(row, col, nextRow, nextCol):
    global count

    absRow = abs(row - nextRow)
    absCol = abs(col - nextCol)
    nextRow += absRow
    nextCol += absCol

    if row >= 0 and row <= rowSize:
        if col >= 0 and col <= colSize:
            if datas[row][col] == "-" and not visited[row][col]:
                count += 1
                visited[row][col] = True
            if datas[row][col] != "#":
                count += 1
    if nextRow >= 0 and nextRow <= rowSize:
        if nextCol >= 0 and nextCol <= colSize:
            if datas[nextRow][nextCol] == "-":
                datas[nextRow][nextCol] = "#"
            if datas[nextRow][nextCol] != "#":
                count += 1

for row in range(len(datas)):
    listRow = datas[row]
    for col in range(len(listRow)):
        antenna = datas[row][col]
        if antenna == "-" or antenna == "#":
            continue
        for nextRow in range(row + 1, len(datas)):
            for nextCol in range(len(datas[0])):
                curAntenna = datas[nextRow][nextCol]
                if curAntenna == antenna:
                    markAntinode(row, col, nextRow, nextCol)

print(count)

from collections import defaultdict

def part2(data):
    _map = [list(line) for line in data]
    rows, cols = len(_map), len(_map[0])
    antennas = defaultdict(list)

    for row in range(rows):
        for col in range(cols):
            if _map[row][col] != ".":
                antennas[_map[row][col]].append((row, col))

    antinodes = set()

    for antenna, coords in antennas.items():
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                diff = tuple(a - b for a, b in zip(coords[j], coords[i]))
                pos = coords[i]

                while 0 <= pos[0] < rows and 0 <= pos[1] < cols:
                    antinodes.add(pos)
                    pos = tuple(a + b * diff for a, b in zip(pos, diff))

    return len(antinodes)

y = part2(datas)
print(y)
