import heapq
from collections import deque

datas = []

with open("Day20.txt", "r") as file:
    
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

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def dijkstra():
    
    startPos = start
    endPos = end
    distance = {startPos: 0}
    p_queue = [(0, startPos)]
    
    while p_queue:
        
        curDist, curPos = heapq.heappop(p_queue)
        if curPos == endPos:
            break
        
        for direction in directions:
            neighbor = (curPos[0] + direction[0], curPos[1] + direction[1])
            if 0 <= neighbor[0] < len(part1Datas) and 0 <= neighbor[1] < len(part1Datas[0]) and part1Datas[neighbor[0]][neighbor[1]] != "#":
                new_dist = curDist + 1
                
                if neighbor not in distance or new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    heapq.heappush(p_queue, (new_dist, neighbor))
                    
    
    return distance

dist = dijkstra()

saved_seconds = []

def bfs():
    startPos = start
    endPos = end
    visited = set()
    queue = deque([(startPos, dist.get(startPos, 0))])  # Initialize with position and cost
    visited.add(startPos)
    saved_seconds = []  # List to store saved seconds
    
    while queue:
        curPos, curCost = queue.popleft()
        
        # If the end position is reached
        if curPos == endPos:
            break
        
        # Explore normal movements
        for direction in directions:
            neighbor = (curPos[0] + direction[0], curPos[1] + direction[1])
            
            if (
                0 <= neighbor[0] < len(part1Datas) and 
                0 <= neighbor[1] < len(part1Datas[0]) and 
                part1Datas[neighbor[0]][neighbor[1]] != "#" and 
                neighbor not in visited
            ):
                visited.add(neighbor)
                queue.append((neighbor, curCost + 1))
            
            # Wall-walking logic
            if (
                0 <= neighbor[0] < len(part1Datas) and 
                0 <= neighbor[1] < len(part1Datas[0]) and 
                part1Datas[neighbor[0]][neighbor[1]] == "#"
            ):
                cheat = (neighbor[0] + direction[0], neighbor[1] + direction[1])
                
                if cheat in dist:  # Ensure cheat position is in dist
                    saved = dist[cheat] - dist[curPos] - 2  # Calculate time saved
                    
                    if saved > 0:
                        saved_seconds.append(saved)
    
    return saved_seconds

result = bfs()
sorted_result = sorted(result)

# Count values greater than 100
count_greater_than_100 = len([value for value in sorted_result if value >= 100])

print(f"Count of values greater than 100: {count_greater_than_100}")

## part 2

part2Datas = datas
