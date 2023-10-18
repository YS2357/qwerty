alpabet = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
word = input()

time = 0
for i in alpabet:
    for j in i:
        for k in word:
            if j == k:
                time += alpabet.index(i) + 3
print(time)