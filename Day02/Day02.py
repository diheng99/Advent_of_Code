with open("Day2.txt", "r") as file:
    
    arrays = [list(map(int, line.split())) for line in file]

def safe_count(array):
    
    inc = all(array[i] < array[i+1] for i in range(len(array) - 1))
    dec = all(array[i] > array[i+1] for i in range(len(array) - 1))
    
    if not inc or not dec:
        return False
    
    for i in range(len(array) - 1):
        diff = abs(array[i] - array[i+1])
        if diff > 3 or diff < 1:
            return False
    
    return True

part1Array = arrays
res = sum(1 for array in part1Array if safe_count(array))

print("Part 1 result is: ", res)

############################# PART 2 ######################################

def safe_count_2(array):
    
    inc = all(array[i] < array[i+1] for i in range(len(array) - 1))
    dec = all(array[i] > array[i+1] for i in range(len(array) - 1))
    
    if not inc or not dec:
        return False
    
    for i in range(len(array) - 1):
        diff = abs(array[i] - array[i+1])
        if diff > 3 or diff < 1:
            return False
    
    return True

def safe_count_3(array):
    if safe_count_2(array):
        return True
    
    for i in range(len(array)):
        newArray = array[:i] + array[i+1:]
        if safe_count_2(newArray):
            return True
        
part2Array = arrays
res = sum(1 for array in part2Array if safe_count_3(array))
print("Part 2 result is: ", res)
