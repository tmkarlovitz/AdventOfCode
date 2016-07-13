import re

nice_strings = []

with open('day5input.txt', 'r') as f:
    for line in f:
        line = line.strip()

        bad_pairs = re.search(r"(ab|cd|pq|xy)", line)
        if bad_pairs != None:
            continue
        vowels = re.findall(r"[aeiou]", line)
        if vowels != None:
            if len(vowels) < 3:
                continue
        double = re.search(r"(.)\1", line)
        if double == None:
            continue
        nice_strings.append(line)

    print(len(nice_strings))
