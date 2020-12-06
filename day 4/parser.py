def parse(item):
    item = item.split(":")
    if item[0] in c:
        return True
    return False


f = open('input.txt', 'r').read().split('\n\n')
l = [ l.replace("\n"," ").split() for l in f]

for item in l:
    print(item)
    
c = ["byr","iyr" ,"eyr","hgt","hcl","ecl","pid"]

t = 0
for item in l:
    if len(item) == 7 and  all(map(parse,item)):
        t+=1  
    elif len(item) == 8:
        t+=1
        
print(t)