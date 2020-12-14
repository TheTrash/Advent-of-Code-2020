f = open('input.txt', 'r')

memory = {}

for line in f.readlines():
    if(line[0:4]=="mask"):
        mask = line.replace("mask = ",'').replace('\n','')
        print(mask)
    else:
        tmp = line.split()
        m_id = int(tmp[0].replace("mem[",'').replace("]",''))
        bit = list(f'{int(tmp[2]):036b}')
        for i, b in enumerate(mask):
            if(b != 'X'):
                bit[i] = b
        memory[m_id] = int(''.join(bit),2)

values = memory.values()
print(sum(values))

