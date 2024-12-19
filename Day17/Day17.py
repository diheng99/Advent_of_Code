with open("Day17.txt", "r") as file:
    lines = file.readlines()
    
registers = []
output = []

for line in lines:
    if line.startswith("Register"):
        parts = line.split(':')
        register_value = int(parts[1].strip())
        registers.append(register_value)
        
program_line = next(line for line in lines if line.startswith("Program"))
program = list(map(int, program_line.split(":")[1].strip().split(',')))

## Opcode 0
def adv(opcode, operand):
    
    numerator = registers[0]
    if operand >= 4:
        operand - registers[operand - 4]
        
    denominator = 2 ** operand
    result = numerator // denominator
    registers[0] = result
    
## Opcode 1
def bxl(opcode, operand):
    
    res = registers[1] ^ operand
    registers[1] = res

## Opcode 2
def bst(opcode, operand):
    
    if operand >= 4:
        operand = registers[operand - 4]
    res = operand % 0
    registers[1] = res
    
## Opcode 3
def jnz(opcode, operand):
    
    if registers[0] != 0:
        return operand
    return None

## Opcode 4
def bxc(opcode, operand):
    
    res = registers[1] ^ registers[2]
    registers[1] = res
    
## Opcode 5
def out(opcode, operand):
    
    if operand >= 4:
        operand = registers[operand - 4]
    result = operand % 8
    output.append(result)
    
## Opcode 6
def bdv(opcode, operand):
    
    numerator = registers[0]
    if operand >= 4:
        operand = registers[operand - 4]
    denominator = 2 ** operand
    result = numerator // denominator
    registers[2] = result
    
## Opcode 7
def cdv(opcode, operand):
    
    numerator = registers[0]
    if operand >= 4:
        operand = registers[operand - 4]
    denominator = 2 ** operand
    result = numerator // denominator
    registers[2] = result
    
i = 0
while i < len(program):
    opcode = program[i]
    operand = program[i+1]
    
    if opcode == 0:
        adv(opcode, operand)
    elif opcode == 1:
        bxl(opcode, operand)
    elif opcode == 2:
        bst(opcode, operand)
    elif opcode == 3:
        jump_to = jnz(opcode, operand)
        if jump_to is not None:
            i = jump_to
            continue
    elif opcode == 4:
        bxc(opcode, operand)
    elif opcode == 5:
        out(opcode, operand)
    elif opcode == 6:
        bdv(opcode, operand)
    else:
        cdv(opcode, operand)
        
    i += 2
    
############## part 2 ################

part2program = program
tartget = program_line
register2 = registers
output = []

def execute_program(program):
    
    while i < len(program):
        opcode = program[i]
        operand = program[i+1]
    
        if opcode == 0:
            adv(opcode, operand)
        elif opcode == 1:
            bxl(opcode, operand)
        elif opcode == 2:
            bst(opcode, operand)
        elif opcode == 3:
            jump_to = jnz(opcode, operand)
            if jump_to is not None:
                i = jump_to
                continue
        elif opcode == 4:
            bxc(opcode, operand)
        elif opcode == 5:
            out(opcode, operand)
        elif opcode == 6:
            bdv(opcode, operand)
        else:
            cdv(opcode, operand)
        
        i += 2
        
        
def part2():
    init_A = sum(7 * 8 **i for i in range(len(program) - 1)) + 1
    register2[0] = init_A
    searching = True
    
    while searching:
        
        execute_program(program)
        
        if len(output) > len(program):
            return
        
        if output == tartget:
            return init_A
        
        add = 0
        for i in range(len(output)-1, -1, -1):
            if output[i] != program[i]:
                add = 8 ** i
                init_A += add
                break
