def input_clear(line):
    line = line.replace(".",'').replace(" bags",'').replace(" bag",'').replace('\n','')
    line = line.split(" contain ")

    line[1] = line[1].split(', ')
    return line


f = open("input.txt", "r")
l = [input_clear(n) for n in f.readlines()]

b = ["shiny gold"]

for i in b:
    for bags in l:
        for bag in bags[1]:
            if (i in bag) and (bags[0] not in b):
                b.append(bags[0])

print(len(b)-1)
print(b)
