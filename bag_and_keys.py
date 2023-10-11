from itertools import product

change = {1:(0, 5, 8),
          2:(1, 2, 7),
          3:(2, 5, 6, 8),
          4:(1, 2, 3),
          5:(0, 3, 4, 5),
          6:(1, 5, 6),
          7:(3, 4, 6, 7),
          8:(2, 7, 8),
          9:(0, 3, 8),
          }

for keys in product([0,1], repeat=9):
    a = [0, 1, 1, 0, 1, 0, 1, 0, 1]
    for n, key in enumerate(keys):
        if key:
            for i in change[n + 1]:
                a[i] = not a[i]
    if sum(a) == 0:
        print(keys)

# result:
#  a1 a2 a3 a4 a5 a6 a7 a8 a9
# (0, 1, 1, 0, 1, 0, 0, 1, 1)
# (0, 1, 1, 1, 0, 1, 1, 0, 0)
