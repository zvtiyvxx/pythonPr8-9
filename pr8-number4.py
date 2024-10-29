необходимые_экзамены = {
    "Информатика": 80,
    "Математика": 85,
    "Русский язык": 75
}

print("""Для определения возможности поступления, необходима информация о
Вас.
Для ввода экзамена и баллов введите их через |: Химия | 40.
Для завершения ввода нажмите Enter.
""")

сданные_экзамены = {}
while True:
    ввод = input("").strip()
    if ввод == "":
        break
    try:
        экзамен, балл = [x.strip() for x in ввод.split("|")]
        сданные_экзамены[экзамен] = int(балл)
    except ValueError:
        print("Ошибка: баллы должны быть целым числом.")
    except IndexError:
        print("Ошибка: вводите данные в формате 'Предмет | Баллы'.")

print("Ваши экзамены:")
for i, (экзамен, балл) in enumerate(сданные_экзамены.items(), start=1):
    print("{}) {} {}".format(i, экзамен, балл))

ok = False
try:
    for необходимый_экзамен, баллы in необходимые_экзамены.items():
        if сданные_экзамены[необходимый_экзамен] < баллы:
            break
    else:
        ok = True
except KeyError:
    print("Ошибка: не сданы все необходимые экзамены.")

print("Вы можете к нам поступить!" if ok else "Увы...")