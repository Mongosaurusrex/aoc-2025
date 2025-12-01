
def part_one():
    position = 50
    count_zero = 0

    with open("input.txt", "r") as input_lines:
        for line in input_lines:
            line = line.strip()
            if not line:
                continue

            direction = line[0]          
            distance = int(line[1:])     

            if direction == 'R':
                position = (position + distance) % 100
            else:  # 'L'
                position = (position - distance) % 100

            if position == 0:
                count_zero += 1

    return count_zero

def part_two():
    position = 50
    count_zero = 0

    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]        # 'L' or 'R'
            distance = int(line[1:])   # number of clicks

            for _ in range(distance):
                if direction == 'R':
                    position = (position + 1) % 100
                else:  # 'L'
                    position = (position - 1) % 100

                if position == 0:
                    count_zero += 1
    
    return count_zero 

print(part_one())
print(part_two())
