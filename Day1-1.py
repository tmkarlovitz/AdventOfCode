moves_dict = {'(': 1, ')': -1}

with open('day1input.txt', 'r') as f:
    day_1_input = f.read()
    input_as_nums = [moves_dict[char] for char in day_1_input]
    answer = sum(input_as_nums)
    print(answer)
