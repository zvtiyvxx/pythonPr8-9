def power(x, y):
    try:
        if y < 0:
            raise ValueError("Степень должна быть неотрицательным числом.")
        elif y == 0:
            return 1
        else:
            return x * power(x, y - 1)
    except RecursionError:
        print("Слишком большая глубина рекурсии!")
        return None
x = int(input("x="))
y = int(input("y="))
print(power(x, y))
