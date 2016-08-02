
w, h = 1000, 1000
grid_lights = [[0 for x in range(w)] for y in range(h)] #set all lights to be off
counter = 0

with open('day6input.txt', 'r') as f:
    for line in f:
        words = line.split()
        if words[0] == 'turn':
            if words[1] == 'off':
                point1 = words[2].split(',')
                point2 = words[4].split(',')
                for x in range(int(point1[0]), int(point2[0])+1):
                    for y in range(int(point1[1]), int(point2[1])+1):
                        grid_lights[x][y] = 0
            else:
                point1 = words[2].split(',')
                point2 = words[4].split(',')
                for x in range(int(point1[0]), int(point2[0])+1):
                    for y in range(int(point1[1]), int(point2[1])+1):
                        grid_lights[x][y] = 1
        else:
            point1 = words[1].split(',')
            point2 = words[3].split(',')
            for x in range(int(point1[0]), int(point2[0])+1):
                for y in range(int(point1[1]), int(point2[1])+1):
                    if grid_lights[x][y] == 0:
                        grid_lights[x][y] = 1
                    else: grid_lights[x][y] = 0
    for x in range(w):
        for y in range(h):
            if grid_lights[x][y] == 1:
                counter += 1
    print(counter)
