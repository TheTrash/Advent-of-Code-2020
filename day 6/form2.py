f = open('input.txt', 'r').read().split('\n\n')
l = [ l.replace("\n"," ").split() for l in f]


s=0
for group in l:
    aux = {}
    
    for p in group:
        for d in p:
            if d not in aux:
                aux[d]=1
            else:
                aux[d]+=1
    #print(aux , len(aux))
    
    print(aux)
    for e in aux:
        if(aux[e] == len(group)):
            s+=1
    print("s",s)