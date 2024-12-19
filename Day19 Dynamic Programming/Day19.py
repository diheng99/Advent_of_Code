towels = []
designs = []
reading_design = False

with open("Day17.txt", "r") as file:
    for line in file:
        if not reading_design:
            towels.extend(line.strip().split(','))
        
        if line.strip() == "":
            reading_design = True
            continue
        
        if reading_design:
            designs.append(line.strip())
    
towelset = set(towel.strip() for towel in towels)

sum = 0

for design in designs:
    dp = [False] * (len(design) + 1)
    dp[0] = True
    
    for i in range(1, len(design) + 1):
        for j in range(i):
            if dp[j] and design[j:i] in towelset:
                dp[i] = True
                break
    
    if dp[len(design)]:
        sum += 1
        
print(sum)

## part 2

sum = 0

for design in designs:
    dp = [0] * (len(design) + 1)
    dp[0] = 1
    
    for i in range(1, len(design) + 1):
        for j in range(i):
            if dp[j] > 0 and design[j:i] in towelset:
                dp[i] += dp[j]
                
    total_permutations = dp[len(design)]
    sum += total_permutations

print(sum)