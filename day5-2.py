
nice_strings = []

with open('day5input.txt', 'r') as f:
    for line in f:
        #Test case 1
        line = line.strip()
        flag = False
        for i in range(len(line)-3):
            if line[i:i+2] in line[i+2:]:
                flag = True
        if flag == False:
            continue

        #Test case 2
        flag2 = False
        for i in range(len(line)-2):
            if line[i] == line[i+2]:
                flag2 = True
        if flag2 == False:
            continue

        nice_strings.append(line)

    print(len(nice_strings))
