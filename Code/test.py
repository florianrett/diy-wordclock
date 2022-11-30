import random

def Explode():
    e = random.randint(1, 10)
    if e == 10:
        e += Explode()
    # print("Explode ", e)
    return e


def roll():
    r = random.randint(1, 10)
    if r == 1:
        re = 0 - Explode()
    elif r == 10:
        re = r + Explode()
    else:
        re = r
    
    # print("rolled ", r, " -> ", re)
    return re

num = 1000000
values = []
for i in range(num):
    r1 = roll()
    r2 = roll()
    # print(r1, r2)
    value = r1 + r2
    value = min(value, 20)
    value = max(value, 0)
    values.append(value)

P = []
txt = "{p:.2f} %"
for i in range(0, 21):
    P.append(txt.format(p = values.count(i) / num * 100))

print(P)