f = open("input.txt", "r")
l = [int(n) for n in f.readlines()]

min = [el for el in l if el <= (2020/3)]
max = [el for el in l if el > (2020/3)]
#print( min )

for el in l:
    for el2 in l:
        for el3 in l:
            if ((el+el2+el3) == 2020):
                print(el, el2,el3,"sum",el+el2+el3,"mul",el*el2*el3)
                break


