import heapq

datas = []
current_set = []

with open("day13.txt", "r") as file:
    for line in file:
        if "Button A" in line:
            parts = line.split(", ")
            x_a = int(parts[0].split("=")[1])
            y_a = int(parts[1].split("=")[1])
            current_set.append([x_a, y_a])
        elif "Button B" in line:
            parts = line.split(", ")
            x_b = int(parts[0].split("=")[1])
            y_b = int(parts[1].split("=")[1])
            current_set.append([x_b, y_b])
        elif "Prize" in line:
            parts = line.split(", ")
            x_p = int(parts[0].split("=")[1])
            y_p = int(parts[1].split("=")[1])
            current_set.append([x_p, y_p])
            datas.append(current_set)
            current_set = []

def dijkstra(prize, moves, max_presses=100):
    pq = [(0, 0, 0)]
    visited = set()
    visited.add((0, 0))

    while pq:
        cost, x, y = heapq.heappop(pq)

        if (x, y) == prize:
            return cost

        for (dx, dy), token_cost in moves:
            for i in range(1, max_presses + 1):
                next_x, next_y = x + dx * i, y + dy * i
                next_cost = cost + token_cost * i

                if next_x > prize[0] or next_y > prize[1]:
                    break

                if (next_x, next_y) not in visited:
                    visited.add((next_x, next_y))
                    heapq.heappush(pq, (next_cost, next_x, next_y))

    return float('inf')

results = []
for data in datas:
    button_a_move = data[0]
    button_b_move = data[1]
    prize = tuple(data[2])

    moves = [
        (button_a_move, 3),
        (button_b_move, 1)
    ]

    min_tokens = dijkstra(prize, moves)
    results.append(min_tokens)

print("Results:", results)

reachable_results = [result for result in results if result != float('inf')]
total_min_tokens = sum(reachable_results)
print(f"Fewest tokens to win all possible prizes: {total_min_tokens}")

####################### PART 2 ########################

def part2(data):
    machines = data.split("\n\n")
    total_coins = 0

    for machine in machines:
        lines = machine.strip().split("\n")
        if len(lines) != 3:
            print(f"Skipping invalid machine data block: {machine}")
            continue

        btn_a_line, btn_b_line, prize_line = lines

        btn_a_coeffs = [int(value[2:]) for value in btn_a_line.split(": ")[1].split(", ")]
        btn_b_coeffs = [int(value[2:]) for value in btn_b_line.split(": ")[1].split(", ")]

        prize_values = [int(value[2:]) + 1000000000000 for value in prize_line.split(": ")[1].split(", ")]

        denominator = btn_b_coeffs[1] * btn_a_coeffs[0] - btn_b_coeffs[0] * btn_a_coeffs[1]

        times_b = (prize_values[1] * btn_a_coeffs[0] - prize_values[0] * btn_a_coeffs[1]) / denominator
        times_a = (prize_values[0] - btn_b_coeffs[0] * times_b) / btn_a_coeffs[0]

        if times_a.is_integer() and times_b.is_integer():
            total_coins += int(times_a) * 3 + int(times_b)

    return total_coins

# Read data from file
with open("day13.txt", "r") as file:
    data = file.read()

print(part2(data))
