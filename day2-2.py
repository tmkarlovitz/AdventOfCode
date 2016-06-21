with open('day2input.txt', 'r') as f:
    total = 0
    for line in f:
        line = line.strip()
        data = line.split('x')
        data = map(int, data)
        data = sorted(data)
        total += 2 * data[0] + 2 * data[1]
        total += data[0] * data[1] * data[2]
    print(total)
