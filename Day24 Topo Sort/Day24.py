from collections import defaultdict, deque

def evaluate_logic(op1, operator, op2):
    if operator == "AND":
        return op1 & op2
    elif operator == "OR":
        return op1 | op2
    elif operator == "XOR":
        return op1 ^ op2

with open("Day24.txt", "r") as file:
    lines = file.readlines()

variables = {}
instructions = []

for line in lines:
    line = line.strip()
    if ":" in line:
        key, value = line.split(":")
        variables[key.strip()] = int(value.strip())
    elif "->" in line:
        parts = line.split("->")
        operation = parts[0].strip().split()
        output = parts[1].strip()
        instructions.append([*operation, output])

resolved = {}

while instructions:
    for instruction in instructions[:]:
        if len(instruction) == 4:
            op1, operator, op2, output = instruction
            if op1.isdigit() or op1 in resolved or op1 in variables:
                operand1 = int(op1) if op1.isdigit() else resolved.get(op1, variables.get(op1))
                if op2.isdigit() or op2 in resolved or op2 in variables:
                    operand2 = int(op2) if op2.isdigit() else resolved.get(op2, variables.get(op2))
                    resolved[output] = evaluate_logic(operand1, operator, operand2)
                    instructions.remove(instruction)

z_values = {key: resolved[key] for key in resolved if key.startswith("z")}
sorted_z_keys = sorted(z_values.keys(), key=lambda k: int(k[1:]), reverse=True)
binary_output = "".join(str(z_values[key]) for key in sorted_z_keys)
decimal_output = int(binary_output, 2)

print("Binary Output (zNN from highest to lowest):", binary_output)
print("Decimal Output:", decimal_output)

## Part 2

import re
from collections import defaultdict

with open("Day24.txt", "r") as f:
    wires_raw, gates_raw = f.read().strip().split("\n\n")

wires = {}
for line in wires_raw.split("\n"):
    name, value = line.split(": ")
    wires[name] = int(value)

input_bit_count = len(wires_raw.split("\n")) // 2

gates = []
for line in gates_raw.split("\n"):
    inputs, output = line.split(" -> ")
    a, op, b = inputs.split(" ")
    gates.append({"a": a, "op": op, "b": b, "output": output})
    if a not in wires:
        wires[a] = None
    if b not in wires:
        wires[b] = None
    if output not in wires:
        wires[output] = None

def is_direct(gate):
    return gate["a"].startswith("x") or gate["b"].startswith("x")

def is_output(gate):
    return gate["output"].startswith("z")

def is_gate(gate, type_):
    return gate["op"] == type_

def has_output(output):
    return lambda gate: gate["output"] == output

def has_input(input_):
    return lambda gate: gate["a"] == input_ or gate["b"] == input_

flags = set()

FAGate0s = [gate for gate in gates if is_direct(gate) and is_gate(gate, "XOR")]
for gate in FAGate0s:
    a, b, output = gate["a"], gate["b"], gate["output"]
    is_first = a == "x00" or b == "x00"
    if is_first:
        if output != "z00":
            flags.add(output)
        continue
    elif output == "z00":
        flags.add(output)
    if is_output(gate):
        flags.add(output)

FAGate3s = [gate for gate in gates if is_gate(gate, "XOR") and not is_direct(gate)]
for gate in FAGate3s:
    if not is_output(gate):
        flags.add(gate["output"])

output_gates = [gate for gate in gates if is_output(gate)]
for gate in output_gates:
    is_last = gate["output"] == f"z{str(input_bit_count).zfill(2)}"
    if is_last:
        if gate["op"] != "OR":
            flags.add(gate["output"])
        continue
    elif gate["op"] != "XOR":
        flags.add(gate["output"])

to_check = []
for gate in FAGate0s:
    output = gate["output"]
    if output in flags:
        continue
    if output == "z00":
        continue
    matches = list(filter(has_input(output), FAGate3s))
    if len(matches) == 0:
        to_check.append(gate)
        flags.add(output)

for gate in to_check:
    a, output = gate["a"], gate["output"]
    intended_result = f"z{a[1:]}"
    matches = list(filter(has_output(intended_result), FAGate3s))
    match = matches[0]
    to_check = [match["a"], match["b"]]
    or_matches = [gate for gate in gates if is_gate(gate, "OR") and gate["output"] in to_check]
    or_match_output = or_matches[0]["output"]
    correct_output = next(output for output in to_check if output != or_match_output)
    flags.add(correct_output)

flags_list = sorted(flags)
print(",".join(flags_list))
