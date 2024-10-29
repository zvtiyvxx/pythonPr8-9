
numbers = []
with open("numbers.txt", "r") as file:
    for line in file:
        try:
            number = float(line.strip())
            numbers.append(number)
        except ValueError:
            print(f"Нельзя преобразовать в число: {line}")

summ = sum(numbers)
max_number = max(numbers)

with open("1.3 numbers.txt", "x") as file:
    file.write(f"Summa chisel: {summ}\n")
    file.write(f"Maksimalnoe chislo: {max_number}")

print("Сумма и максимальное число записаны в конец файла.")
