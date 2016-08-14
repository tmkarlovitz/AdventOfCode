line_list = []
val_dict = {}
know_dict = {}
done_line = {}
commands = ['AND', 'RSHIFT', 'LSHIFT', 'OR', 'NOT', '->']

with open('day7input.txt', 'r') as f:
    for line in f:
        line_list.append(line)
        done_line[line] = False
        linedata = line.split()
        for word in linedata:
            if not word in commands:
                if not word.isdigit():
                    val_dict[word] = 0
                    know_dict[word] = False

    while all(know_dict.values()) == False:
        for line in line_list:
            if done_line[line]: continue
            linedata = line.split()
            if linedata[0] == 'NOT':
                if linedata[1].isdigit() or know_dict[linedata[1]]:
                    val_dict[linedata[3]] = ~val_dict[linedata[1]]
                    know_dict[linedata[3]] = True
                    done_line[line] = True
                else: continue
            elif linedata[1] == 'AND':
                if linedata[0].isdigit():
                    firstValue = int(linedata[0])
                elif know_dict[linedata[0]]:
                    firstValue = val_dict[linedata[0]]
                else: continue
                if linedata[2].isdigit():
                    secondValue = int(linedata[2])
                elif know_dict[linedata[2]]:
                    secondValue = val_dict[linedata[2]]
                else: continue
                val_dict[linedata[4]] = firstValue & secondValue
                know_dict[linedata[4]] = True
                done_line[line] = True
            elif linedata[1] == 'OR':
                if linedata[0].isdigit():
                    firstValue = int(linedata[0])
                elif know_dict[linedata[0]]:
                    firstValue = val_dict[linedata[0]]
                else: continue
                if linedata[2].isdigit():
                    secondValue = int(linedata[2])
                elif know_dict[linedata[2]]:
                    secondValue = val_dict[linedata[2]]
                else: continue
                val_dict[linedata[4]] = firstValue | secondValue
                know_dict[linedata[4]] = True
                done_line[line] = True
            elif linedata[1] == 'RSHIFT':
                if linedata[0].isdigit():
                    firstValue = int(linedata[0])
                elif know_dict[linedata[0]]:
                    firstValue = val_dict[linedata[0]]
                else: continue
                val_dict[linedata[4]] = firstValue >> int(linedata[2])
                know_dict[linedata[4]] = True
                done_line[line] = True
            elif linedata[1] == 'LSHIFT':
                if linedata[0].isdigit():
                    firstValue = int(linedata[0])
                elif know_dict[linedata[0]]:
                    firstValue = val_dict[linedata[0]]
                else: continue
                val_dict[linedata[4]] = firstValue << int(linedata[2])
                know_dict[linedata[4]] = True
                done_line[line] = True
            elif linedata[1] == '->':
                if not linedata[0].isdigit():
                    if know_dict[linedata[0]]:
                        val_dict[linedata[2]] = int(val_dict[linedata[0]])
                        know_dict[linedata[2]] = True
                        done_line[line] = True
                else:
                    val_dict[linedata[2]] = int(linedata[0])
                    know_dict[linedata[2]] = True
                    done_line[line] = True

    print(val_dict['a'])
