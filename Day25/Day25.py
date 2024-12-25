locks_schematics = []
pins_schenatics = []
locks_header = '#####'
pins_header = '.....'

with open("Day25.txt", "r") as file:
    data = file.read().split("\n\n")

for schematic in data:
    schematic_lines = schematic.split("\n")
    header = schematic_lines[0]

    num_columns = len(header)
    column_counts = [0] * num_columns


    if header == locks_header:

        for row in schematic_lines[1:]: 
            for col_index, char in enumerate(row):
                if char == "#":
                    column_counts[col_index] += 1

        locks_schematics.append(column_counts)
    else:

        for row in schematic_lines[1: len(schematic_lines) - 1]: 
            for col_index, char in enumerate(row):
                if char == "#":
                    column_counts[col_index] += 1
                
        pins_schenatics.append(column_counts)

count = 0

for pins in pins_schenatics:

    for lock in locks_schematics:

        valid = True
        for i, char in enumerate(pins):
            if int(pins[i]) + int(lock[i]) > 5:
                valid = False
                break
        
        if valid:
            count += 1

print(count)
