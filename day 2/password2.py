def password(li):
    #['11', '16', 'n', 'tnsznnfscnwtsdwn']
    li = li.replace('-', ' ').replace(':', '').split()
    #print(li)
    #-1 for the [0;n-1] len
    li[0] = int(li[0])-1
    li[1] = int(li[1])-1

    st = str(li[3])
    
    if ((li[2][0] == st[li[0]]) and (li[2][0] != st[li[1]])):
        print(li[2],st[li[0]], st[li[1]])
        return True
    elif ((li[2][0] == st[li[1]]) and (li[2][0] != st[li[0]])):
        print(li[2],st[li[0]], st[li[1]])
        return True
    return False

f = open("input.txt", "r")
l = [str(n).replace('\n', '') for n in f.readlines()]

result = [ n for n in l if password(n)]
print(len(result))
#min = [el for el in l if el < 1010]
