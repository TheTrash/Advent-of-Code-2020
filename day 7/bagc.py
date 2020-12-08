def input_clear(line):
    line = line.replace(".",'').replace(" bags",'').replace(" bag",'').replace('\n','')
    line = line.split(" contain ")

    line[1] = line[1].split(', ')
    return line

f = open("input.txt", "r")
l = [input_clear(n) for n in f.readlines()]


b = ["shiny gold"]

def check(bag):
    for b in l:
        if bag == b[0]:


s = 0
for i in b:
    for bags in l:
        print(i,bags[0])
        if i == bags[0]:
            for bag in bags[1]:
                print(bag)
                tmp = bag.split()
                s += 
            

print(s)