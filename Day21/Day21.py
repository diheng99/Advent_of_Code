numeric_keypad = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
    '0': (3, 1), 'A': (3, 2)
}

robot_keypad = {
    '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2)
}

directions = {
    (-1, 0): '^',  
    (1, 0): 'v',   
    (0, -1): '<',  
    (0, 1): '>'    
}

def calculate_commands_for_robot1(target_sequence):
    current_position = numeric_keypad['A']
    command_sequence = []
    
    for target in target_sequence:
        target_position = numeric_keypad[target]
        row_diff = target_position[0] - current_position[0]
        col_diff = target_position[1] - current_position[1]
        
        if row_diff != 0:
            command_sequence.extend([directions[(1 if row_diff > 0 else -1, 0)]] * abs(row_diff))
        
        if col_diff != 0:
            command_sequence.extend([directions[(0, 1 if col_diff > 0 else -1)]] * abs(col_diff))
        
        command_sequence.append('A')
        current_position = target_position

    return command_sequence

def translate_commands(current_commands, keypad, current_position):
    translated_commands = []
    for command in current_commands:
        if command not in keypad:
            continue
        
        target_position = keypad[command]
        row_diff = target_position[0] - current_position[0]
        col_diff = target_position[1] - current_position[1]
        
        if row_diff != 0:
            direction = directions[(1 if row_diff > 0 else -1, 0)]
            translated_commands.extend([direction] * abs(row_diff))
        
        if col_diff != 0:
            direction = directions[(0, 1 if col_diff > 0 else -1)]
            translated_commands.extend([direction] * abs(col_diff))
        
        translated_commands.append('A')
        current_position = target_position  

    return translated_commands


def calculate_complexity_with_robots(codes):
    total_complexity = 0
    
    for code in codes:
        numeric_part = int(code[:-1])  
        commands_robot1 = calculate_commands_for_robot1(code)
        commands_robot2 = translate_commands(commands_robot1, robot_keypad, robot_keypad['A'])
        commands_robot3 = translate_commands(commands_robot2, robot_keypad, robot_keypad['A'])

        robot3_command_count = len(commands_robot3)
        complexity = robot3_command_count * numeric_part
        total_complexity += complexity
    
    return total_complexity

codes = ["869A", "170A", "319A", "349A", "489A"]

total_complexity = calculate_complexity_with_robots(codes)
print(f"Total Complexity: {total_complexity}")
