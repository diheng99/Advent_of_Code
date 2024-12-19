import heapq, sys
from collections import deque, defaultdict

datas = []

with open("Day16.txt", "r") as file:
    for line in file:
        datas.append(list(line.strip()))

part1Datas = datas

def findStart():
    for row in range(len(part1Datas)):
        for col in range(len(part1Datas[0])):
            if part1Datas[row][col] == "S":
                return (row, col)
            
def findEnd():
    for row in range(len(part1Datas)):
        for col in range(len(part1Datas[0])):
            if part1Datas[row][col] == "E":
                return (row, col)

start = findStart()
end = findEnd()

print("start, end is located at", start, end)

direction_names = ['N', 'E', 'S', 'W']
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

memo = {}

def bfs(data, start, endPos):
    stack = [(start, 1, 0)]
    memo[(start, 1)] = 0
    
    while stack:
        curPos, curDir, curCost = stack.pop()
        
        ## Base Case -> pos = End
        if curPos == endPos:
            continue
        
        ## Second Case -> Check 4 directions
        
        for i, curDirection in enumerate(directions):
            neighbor = (curPos[0] + curDirection[0], curPos[1] + curDirection[1])
            
            if 0 < neighbor[0] < len(part1Datas) and 0 < neighbor[1] < len(part1Datas[0]) and part1Datas[neighbor[0]][neighbor[1]] != "#":
                if i == curDir:
                    newCost = 1
                else:
                    newCost = 1000 + 1
                
                total_cost = curCost + newCost
                if (neighbor, i) not in memo or total_cost < memo[(neighbor, i)]:
                    memo[(neighbor, i)] = total_cost
                    stack.append((neighbor, i, total_cost))
    
    min_cost = min(memo.get((end, i), sys.maxsize) for i in range(4))
    return min_cost

result = bfs(part1Datas, start, end)
print("part 1 result: ", result)