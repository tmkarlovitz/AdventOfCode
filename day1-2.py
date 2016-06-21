moves_dict = {'(': 1, ')': -1}

with open('day1input.txt', 'r') as f:
    day_1_input = f.read()
    input_as_nums = [moves_dict[char] for char in day_1_input]

current_floor = 0
for idx, num in enumerate(input_as_nums):
    current_floor += num
    if current_floor < 0:
        print idx + 1
        break
