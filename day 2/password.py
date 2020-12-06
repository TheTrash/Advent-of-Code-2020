def password(li):
    li = li.replace('-', ' ').replace(':', '').split()
    li[0] = int(li[0])
    li[1] = int(li[1])
    c = li[3].count(li[2])
    if (li[0] <= c and c <= li[1]):
        return True
    return False

f = open("input.txt", "r")
l = [str(n).replace('\n', '') for n in f.readlines()]

result = [ n for n in l if password(n)]
print(len(result))
#min = [el for el in l if el < 1010]

