map = []
moves = []

reading_map = True

with open("Day15.txt", "r") as file:
    for line in file:
        line = line.strip()
        
        if line == "":
            reading_map = False
            continue
        
        if reading_map:
            map.append(list(line))
            
        else:
            moves.append(list(line))
        
def findRobot():
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] == "@":
                return row, col
            
rowPos, colPos = findRobot()

def moveLeft(row, col, sym):
    newCol = col - 1
    
    if newCol < 0:
        return row, col
    
    if map[row][newCol] == "#":
        return row, col
    
    if map[row][col] == "O":
        nextRow, nextCol = moveLeft(row, newCol, "O")
        if (nextRow, nextCol) != (row, col):
            map[row][col] = "."
            map[row][newCol] = sym
            return row, newCol
        else:
            return row, col
        
    return row, col

def moveUp(row, col, sym):
    newRow = row - 1
    
    if newRow < 0:
        return row, col
    
    if map[newRow][col] == ".":
        map[row][col] = "."
        map[newRow][col] = sym
        return newRow, col
    
    if map[newRow][col] == "#":
        return row, col
    
    if map[newRow][col] == "O":
        nextRow, nextCol = moveUp(newRow, col, "O")
        if (nextRow, nextCol) != (newRow, col):
            map[row][col] = "."
            map[newRow][col] = sym
            return newRow, col
        else:
            return row, col
        
    return row, col

def moveRight(row, col, sym):
    newCol = col + 1
    
    if newCol >= len(map[row]):
        return row, col
    
    if map[row][newCol] == ".":
        map[row][col] = "."
        map[row][newCol] = sym
        return row, newCol
    
    if map[row][newCol] == "#":
        return row, col
    
    if map[row][newCol] == "O":
        nextRow, nextCol = moveRight(row, newCol, "O")
        if (nextRow, nextCol) != (row, newCol):
            map[row][col] = "."
            map[row][newCol] = sym
            return row, newCol
        else:
            return row, col
    
    return row, col

def moveDown(row, col, sym):
    newRow = row + 1
    
    if newRow >= len(map):
        return row, col
    
    if map[newRow][col] == ".":
        map[row][col] = "."
        map[newRow][col] = sym
        return newRow, col
    
    if map[newRow][col] == "#":
        return row, col
    
    if map[newRow][col] == "#":
        return row, col
    
    if map[newRow][col] == "O":
        nextRow, nextCol = moveDown(newRow, col, "O")
        if (nextRow, nextCol) != (newRow, col):
            map[row][col] = "."
            map[newRow][col] = sym
            return newRow, col
        else:
            return row, col
        
    return row, col

def newMap():
    
    sum = 0
    
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "O":
                sum += 100 * i + j
                
def moving():
    global rowPos, colPos
    for row in range(len(moves)):
        for col in range(len(moves[row])):
            if moves[row][col] == "<":
                rowPos, colPos = moveLeft(rowPos, colPos, "@")
            if moves[row][col] == "^":
                rowPos, colPos = moveUp(rowPos, colPos, "@")
            if moves[row][col] == ">":
                rowPos, colPos = moveUp(rowPos, colPos, "@")
            if moves[row][col] == "v":
                rowPos, colPos = moveUp(rowPos, colPos, "@")
    
    newMap()