present_count = {}
current_x = 0
current_y = 0
present_count[(current_x,current_y)] = 1

with open('day3input.txt', 'r') as f:
    day_3_input = f.read()
    for char in day_3_input:
        if char == '^': current_y += 1
        if char == 'v': current_y -= 1
        if char == '<': current_x -= 1
        if char == '>': current_x += 1
        if(current_x, current_y) in present_count:
            present_count[(current_x, current_y)] += 1
        else:
            present_count[(current_x,current_y)] = 1

print len(present_count)
