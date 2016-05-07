input_file = open('day1input.txt', 'r')
day_1_input = input_file.read()

moves_dict = {'(': 1, ')': -1}
input_as_nums = [moves_dict[char] for char in day_1_input]

current_floor = 0
for idx, num in enumerate(input_as_nums):
    current_floor += num
    if current_floor < 0:
        print idx + 1
        break
