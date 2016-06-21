with open('day2input.txt', 'r') as f:
    total = 0
    for line in f:
        line = line.strip()
        data = line.split('x')
        data = map(int, data)
        a = data[0] * data[1]
        b = data[0] * data[2]
        c = data[1] * data[2]
        total += 2 * a + 2 * b + 2 * c
        smallest = a
        if(b < smallest): smallest = b
        if(c < smallest): smallest = c
        total += smallest

    print(total)
