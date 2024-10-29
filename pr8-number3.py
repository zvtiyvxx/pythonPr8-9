try:
    n = int(input("Введите кол-во человек: "))
    if n < 0:
        raise ValueError("Количество должно быть неотрицательным числом.")
    else:
        middle_names = {}
        for i in range(n):
            fio = input("Введите ФИО через пробел: ").split()

            middle_name = fio[2]
            middle_names[middle_name] = middle_names.get(middle_name, 0) + 1
    print(sorted(middle_names.items(), key=lambda item: item[1])[-1][0])
    print("В расчете участвовало человек:", n)
except IndexError as ie:
    print("Ошибка ввода ФИО:", ie)