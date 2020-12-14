from itertools import product
li=['0','1']

f = open('input.txt', 'r')

memory = {}

for line in f.readlines():
    if(line[0:4]=="mask"):
        mask = line.replace("mask = ",'').replace('\n','')
        print(mask)
    else:
        array = line.split()
        m_id = int(array[0].replace("mem[",'').replace("]",''))
        id = f'{int(m_id):036b}'
        #print(id)
        id = list(id)
        for i, b in enumerate(mask):
            if(b == '1'):
                id[i]=1
        #print(''.join(str(n) for n in id))
        tmp = ''
        leng = len(mask.split('X'))
        l = list(mask)
        for comb in product(li, repeat=leng):
            tmp = ''.join(comb)
            t=0
            for i in range(len(l)):
                if l[i] == "X":
                    id[i] = tmp[t]
                    t+=1
            memory[int(''.join(str(n) for n in id),2)] = int(array[2])

print(memory)


values = memory.values()
print(sum(values))

