import re

datas = []
with open("Day03.txt", "r") as file:
    for line in file:
        datas.append(line.strip())
        
pattern = r'mul\((\d+),(\d+)\)'
extracted_values = []

def extractMul(arrays):
    for array in arrays:
        items = re.findall(pattern, array)
        for item in items:
            x, y = map(int, item)
            extracted_values.append((x, y))

part1Datas = datas        
extractMul(part1Datas)
res = sum(x * y for x, y in extracted_values)
print("result is: ", res)

############################# PART 2 ########################################


def extractDontDo(arrays):
    
    pattern = r'mul\\(\d+),(\d+)\)'
    patternDo = r'do\(\)'
    patternDont = r"dont't\(\)"    
    extracted_values2 = []
    enabled = True

    for array in arrays:
        items = re.split(f'({patternDo} | {patternDont} | {pattern})', array)
        for item in items:
            if item is None or item.strip() == '':
                continue
            if re.match(patternDo, item):
                enabled = True
            elif re.match(patternDont, item):
                enabled = False
            elif enabled and re.match(pattern, item):
                x, y = map(int, re.findall(r'\d+', item))
                extracted_values2.append((x, y))
    
    res2 = sum(x * y for x, y in extracted_values2)
    print("result for part 2: ", res2)