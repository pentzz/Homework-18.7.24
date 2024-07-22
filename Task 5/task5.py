# Task a
a: list[int] = [1, 2, 3, 4]
print(len(a))
# Task b
while True:
    try:
        ind: int = int(input("Please enter the index number: "))
        if ind == -999:
            break
        print(f"The number in index {ind} is {a[ind]}.")
    except Exception as e:
        print(f'Something went wrong:  --{e}-- \nPlease try again..')

