# Task a
x: list[int] = []
for i in range(80, 100):
    x.append(i)
# Task b
print(x[0])
# Task c
print(x[-1])
# Task d
print(len(x))
# Task e
print(x[3:12])
# Task f
print(x[3:])
# Task g
print(x[:10])
# Task h
x.insert(int(len(x) / 2), 999)
# Task i
print(x[::-1])
# Task j
print(x[1::2])
