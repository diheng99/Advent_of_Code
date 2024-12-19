datas = []
with open("Day04.txt", "r") as file:
    for line in file:
        datas.append(line.strip())
        
def find_xmas(arrays):
    
    array = arrays[:]
    
    for i in range(len(arrays[0])):
        transpose_col = "".join([row[i] for row in arrays])
        array.append(transpose_col)
        
    def find_diagonals(inputArray):
        row, col = len(inputArray), len(inputArray[0])
        diagonals = {}
        anti_diagonals = {}
        
        for r in range(row):
            for c in range(col):
                diagonal_key = r - c
                if diagonal_key not in diagonals:
                    diagonals[diagonal_key] = []
                diagonals[diagonal_key].append(inputArray[r][c])
                
                anti_diagonals_key = r + c
                if anti_diagonals_key not in anti_diagonals:
                    anti_diagonals[anti_diagonals_key] = []
                anti_diagonals[anti_diagonals_key].append(inputArray[r][c])
                
        return diagonals, anti_diagonals 
    
    diagonal, anti_diagonal = find_diagonals(arrays)   
    
    for diag in diagonal.values():
        array.append("".join(diag))
    for diag in anti_diagonal.values():
        array.append("".join(diag))
        
    count = 0
    for data in array:
        count += data.count("XMAS") + data.count("SAMX")
        
    return count

part1Datas = datas
result = find_xmas(part1Datas)
print("Part 1 result: ", result)

########################## PART 2 ###############################

def part2(arrays):
    rows, cols = len(arrays), len(arrays[0])
    count = 0
    
    _set = {"M", "S"}
    
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if arrays[r][c] == "A":
                if {arrays[r-1][c-1], arrays[r+1][c+1]} == _set and {arrays[r-1][c+1], arrays[r+1][c-1]} == _set:
                    count += 1
                    
    return count

part2Datas = datas
res = part2(part2Datas)
print("Part 2 result is", res)
                    