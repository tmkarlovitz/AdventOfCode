present_count = {}
Santa_x = 0
Santa_y = 0
Robo_x = 0
Robo_y = 0

present_count[(0,0)] = 1

with open('day3input.txt', 'r') as f:
    day_3_input = f.read()
    Santa_input = day_3_input[::2]
    Robo_input = day_3_input[1::2]
    for char in Santa_input:
        if char == '^': Santa_y += 1
        if char == 'v': Santa_y -= 1
        if char == '<': Santa_x -= 1
        if char == '>': Santa_x += 1
        if(Santa_x, Santa_y) in present_count:
            present_count[(Santa_x, Santa_y)] += 1
        else:
            present_count[(Santa_x,Santa_y)] = 1
    for char in Robo_input:
        if char == '^': Robo_y += 1
        if char == 'v': Robo_y -= 1
        if char == '<': Robo_x -= 1
        if char == '>': Robo_x += 1
        if(Robo_x, Robo_y) in present_count:
            present_count[(Robo_x, Robo_y)] += 1
        else:
            present_count[(Robo_x, Robo_y)] = 1

print len(present_count)
