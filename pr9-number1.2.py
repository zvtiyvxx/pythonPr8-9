
numbers = []
with open("numbers.txt", "r") as file:
    for line in file:
        number = float(line.strip())
        numbers.append(number)

summ = sum(numbers)
max_number = max(numbers)

with open("numbers.txt", "a") as file:
    file.write(f"\nSumma chisel: {summ}\n")
    file.write(f"Maksimalnoe chislo: {max_number}")

print("Сумма и максимальное число записаны в конец файла.")
