numbers = input("Введите вещественные числа, разделенные пробелами: ").split()

with open("numbers.txt", "w") as file:
    for number in numbers:
        try:
            float_number = float(number)
            file.write(f"{float_number}\n")
        except ValueError:
            print(f"'{number}' не является вещественным числом и будет пропущено.")

print("Числа успешно записаны в файл numbers.txt.")