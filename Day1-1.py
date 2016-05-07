input_file = open('day1input.txt', 'r')
day_1_input = input_file.read()

moves_dict = {'(': 1, ')': -1}

input_as_nums = [moves_dict[char] for char in day_1_input]
answer = sum(input_as_nums)

print(answer)
