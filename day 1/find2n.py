f = open("input.txt", "r")
l = [int(n) for n in f.readlines()]

min = [el for el in l if el < 1010]
max = [el for el in l if el > 1010]

for el in min:
    for m in max:
        sum = el + m
        if sum == 2020:
            print(el,m, "sum ->", sum, "mult->", (el*m))
            break


