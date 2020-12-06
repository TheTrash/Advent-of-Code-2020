f = open('input.txt', 'r').read().split('\n\n')
l = [ l.replace("\n"," ").split() for l in f]

s=0
for group in l:
    aux = []
    for p in group:
        for d in p:
            if d not in aux:
                aux.append(d)
    s += len(aux)
    #print(aux , len(aux))
    print("-")
print(s)