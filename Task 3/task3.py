import random
# Task a
a: list[bool] = []
for i in range(0,3):
    a.append(random.choice([True,False]))
print(a)
# Task b
print(all(a))
# Task c
print(any(a))
# Task d
print(not any(a))
# Task e
print(not all(a))
# Task f
b: list[int] = [random.randint(-2, 2) for i in range(0, 5)]
# Task g
print(b)
print(f"True" if all(b) != 0 else "False")
# Task h
print(f"True" if any(b) != 0 else "False")
# Task i
print(f"True" if not any(b) != 0 else "False")
# Task j
print(f"True" if not all(b) != 0 else "False")