import statistics

# Task a
x: list[float] = []
# Task b
while True:
    temp = float(input("Please enter the temperature: "))
    if temp == -999:
        break
    if temp > 50 or temp < -50:
        continue
    x.append(temp)
# Task c
x.extend([-20.0, 39.1, 18.5])
print(x)
# Task d
print(f"The max temperature is: {max(x)}")
# Task e
print(f"The min temperature is: {min(x)}")
# Task f
print(f"The avg of the temperatures is: {sum(x)/len(x)}")
# Task g
print(f"The avg of the temperatures is: {statistics.mean(x)}")
# Task h
del x[0]
# Task i
x.remove(18.5)
# Task j
last_temp: float = x.pop(len(x)-1)
# Task k
copy_list: list = x.copy()
copy_list.sort()
# Task l
copy_list2: list = copy_list.copy()
copy_list2.reverse()
# Task m
# ההבדל בין sort ל sorted הוא שפונקציית sort מסדרת ושומרת את הרשימה לאחר
# הפעולה, לעומת sorted שמאפשרת להציג את הרשימה כרשימה מסודרת ללא שמירה של השינויים.

# Task n
# הפונקציה reversed מחזירה אובייקט( מסוג reversed), שהוא אובייקט איטרטור המאפשר לעבור על הרשימה בסדר הפוך.
#  כדי להפוך את האובייקט הזה לרשימה, צריך להשתמש בפונקציה list.
# דוגמא :
# שימוש ב reversed:
# reversed_numbers = reversed(numbers)
#
# הפיכת reversed לרשימה
# reversed_list = list(reversed_numbers)
