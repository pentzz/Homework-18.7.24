import random
# Task a
a: list[int] = [i for i in range(95, 106)]
print(a)
# Task b
b: list[int] = [i for i in range(10, 21,2)]
print(b)
# Task c
c: list[bool] = [random.choice([True, False]) for _ in range(1, 6)]
print(c)
# Task d
#השימוש ב-_ עוזר לשמור על קוד נקי, קריא וברור בכך שהוא מסמן לכותבי הקוד או לקוראים שלו שהוא לא חשוב,
# מונע בלבול עם משתנים אחרים ומשפר את ההבנה של הכוונה מאחורי הקוד.
# הסימן '_' משמש בעיקר למשתנים זמניים
# Task e
e: list[int] = [random.randint(1,100) for _ in range(1, 11)]
print(e)
# Task f
f: list[int] = [_ for _ in e if _ % 2 == 0]
print(f)
# Task g
ev_num: list[int] = [n for n in (random.randint(1, 100) for _ in range(10)) if n % 2 == 0]
print(ev_num)
# Task h
chain: str = input("Please enter a string: ")
ans: list[str] = [_ for _ in chain if _ != "t" and _ != " "]
print(ans)
