from itertools import product
string = "X010011010110000001XX001000XX0000101"
test =   list("000000000000000000000000000000000000")
index = []
li=['0','1']
l = list(string)
leng = len(string.split('X'))
tmp = ''
for comb in product(li, repeat=leng):
    tmp = ''.join(comb)
    print(tmp)
    t=0
    for i in range(len(l)):
         if l[i] == "X":
            test[i]= tmp[t]
            t+=1
    index.append(''.join(test))

for e in index:
    print(int(e,2))
    