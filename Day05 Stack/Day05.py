order_rules = {}
update = False
updates = []
results = []
result2 = []

with open("day5.txt", "r") as file:
    for line in file:
        line = line.strip()

        if not line:
            update = True
            continue

        if not update:
            x, y = line.split("|")
            if x not in order_rules:
                order_rules[x] = []
            order_rules[x].append(y)
        else:
            line = line.split(",")
            updates.append(line)

for update in updates:
    newSet = set()
    flag = False

    for i in range(len(update)):
        newSet.add(update[i])

        if any(value in newSet for value in order_rules.get(update[i], [])):
            flag = True

    if flag:
        break

    if not flag:
        results.append(update)
    else:
        result2.append(update)

sum = 0
for result in results:
    mid = len(result) // 2
    sum += int(result[mid])

print(sum)

##### PART 2 #####
result3 = []

def traverse(element, updateSet, visited, stack):
    visited.add(element)

    for neighbours in order_rules.get(element, []):
        if neighbours not in visited and neighbours in updateSet:
            traverse(neighbours, updateSet, visited, stack)
    stack.append(element)

for update in result2:
    visited = set()
    updateSet = set(update)
    stack = []

    for element in update:
        if element not in visited:
            traverse(element, updateSet, visited, stack)
    
    result3.append(stack[::-1])

sum = 0
for result in result3:
    mid = len(result) // 2
    sum += int(result[mid])

print(sum)
