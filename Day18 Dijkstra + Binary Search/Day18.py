import heapq

datas = []
with open("Day18.txt", "r") as file:
    for _ in range(1024):
        line = file.readline()
        if not line:
            break
        datas.append(list(line.strip().split(',')))

part1datas = datas

total_row = total_col = 70

matrix = [["." for _ in range(total_col + 1)] for _ in range(total_row + 1)]

for data in part1datas:
    x_pos = data[1]
    y_pos = data[0]
    matrix[int(x_pos)][int(y_pos)] = "#"

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def dijkstra():
    
    pos = (0, 0)
    distance = {pos: 0}
    p_queue = [(0, pos)]
    
    while p_queue:
        
        curDist, curPos = heapq.heappop(p_queue)
        
        if curPos == (70, 70):
            break
        
        for dir in directions:
            neighbor = (curPos[0] + dir[0], curPos[1] + dir[1])
            
            if 0 <= neighbor[0] < total_row and 0 <= neighbor[1] < total_col and matrix[neighbor[0]][neighbor[1]] != "#":
                
                new_dist = curDist + 1
                
                if neighbor not in distance or new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    heapq.heappush(p_queue, (new_dist, neighbor))
        
        return distance

dist = dijkstra()

print(f"Result for part 1 is: {dist.get(70, 70)}")

## Part 2

part2Datas = []

with open("Day18.txt", "r") as file:
    for line in file:
        part2Datas.append(list(line.strip().split(',')))
        
def dijkstra():
    
    pos = (0, 0)
    distance = {pos: 0}
    p_queue = [(0, pos)]
    
    while p_queue:
        
        curDist, curPos = heapq.heappop(p_queue)
        
        if curPos == (70, 70):
            break
        
        for dir in directions:
            neighbor = (curPos[0] + dir[0], curPos[1] + dir[1])
            
            if 0 <= neighbor[0] < total_row and 0 <= neighbor[1] < total_col and matrix[neighbor[0]][neighbor[1]] != "#":
                
                new_dist = curDist + 1
                
                if neighbor not in distance or new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    heapq.heappush(p_queue, (new_dist, neighbor))
        
        return distance
    
for i in range(len(part2Datas)):
    
    cur_set = part2Datas[:i+1]
    
    matrix = [["." for _ in range(total_col + 1)] for _ in range(total_row + 1)]
    
    for cur_bytes in cur_set:
        x_pos = cur_bytes[1]
        y_pos = cur_bytes[0]
        matrix[int(x_pos)][int(y_pos)] = "#"
    
    dist = dijkstra()
    
    if (70, 70) not in dict:
        break