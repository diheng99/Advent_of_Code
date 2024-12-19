filename = 'day14.txt'
parts = []
totalRow, totalCol = 103, 101
grid = [[0 for _ in range(totalCol)] for _ in range(totalRow)]

def start(col, row, moveCol, moveRow):
    for i in range(100):
        newRow = row + moveRow
        newCol = col + moveCol

        if newRow >= totalRow:
            newRow = newRow % totalRow
        elif newRow < 0:
            newRow = totalRow + newRow

        if newCol >= totalCol:
            newCol = newCol % totalCol
        elif newCol < 0:
            newCol = totalCol + newCol

        row, col = newRow, newCol

        if i == 99:
            grid[newRow][newCol] += 1

with open(filename, 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            segments = line.split(';')
            if len(segments) == 2:
                p_part = segments[0].split('=')[-1]
                v_part = segments[1].split('=')[-1]

                p_tuple = tuple(map(int, p_part.split(',')))
                v_tuple = tuple(map(int, v_part.split(',')))

                col, row = p_tuple
                moveCol, moveRow = v_tuple

                start(col, row, moveCol, moveRow)

midRow = totalRow // 2
midCol = totalCol // 2

quadrant1 = sum(grid[r][c] for r in range(midRow) for c in range(midCol + 1, totalCol))
quadrant2 = sum(grid[r][c] for r in range(midRow) for c in range(midCol))
quadrant3 = sum(grid[r][c] for r in range(midRow + 1, totalRow) for c in range(midCol))
quadrant4 = sum(grid[r][c] for r in range(midRow + 1, totalRow) for c in range(midCol + 1, totalCol))

safety_factor = quadrant1 + quadrant3 - quadrant2 - quadrant4
print(f"Safety Factor: {safety_factor}")