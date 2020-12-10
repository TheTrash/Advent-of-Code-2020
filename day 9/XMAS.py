f = open("input.txt", "r")
l = [int(n) for n in f.readlines()]

def check_sum(n,li):
    for a in li:
        tmp = n - a
        for b in li:
            if b == tmp:
                return True
    return False

for i in range(25,len(l)):
    #print(l[i],":")
    if( not check_sum(l[i],l[i-25:i])):
        print(l[i])
        break
