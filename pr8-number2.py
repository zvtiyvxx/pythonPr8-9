class Пицца:
    def __init__(self):
        self.название = "Заготовка"
        self.тесто = "тонкое"
        self.соус = "кетчуп"
        self.начинка = []
        self.цена = 0

    def __str__(self):
        return (f"Пицца: {self.название} | Цена: {self.цена:.2f} р.\n"
                f"Тесто: {self.тесто} Соус: {self.соус}\n"
                f"Начинка: {', '.join(self.начинка)}")

    def подготовить(self):
        print(f"Начинаю готовить пиццу {self.название}")
        print(f"  - замешиваю {self.тесто} тесто...")
        print(f"  - добавляю соус: {self.соус}...")
        print(f"  - и, конечно: {', '.join(self.начинка)}...")

    def испечь(self):
        print("Выпекаю пиццу... Готово!")

    def нарезать(self):
        print("Нарезаю на аппетитные кусочки...")

    def упаковать(self):
        print("Упаковываю в фирменную упаковку и готово!")


class ПиццаПепперони(Пицца):
    def __init__(self):
        super().__init__()
        self.название = "Пепперони"
        self.тесто = "тонкое"
        self.соус = "томатный"
        self.начинка = ["пепперони", "сыр моцарелла"]
        self.цена = 350


class ПиццаБарбекю(Пицца):
    def __init__(self):
        super().__init__()
        self.название = "Барбекю"
        self.тесто = "тонкое"
        self.соус = "барбекю"
        self.начинка = ["бекон", "ветчина", "зелень", "сыр моцарелла"]
        self.цена = 450


class ПиццаДарыМоря(Пицца):
    def __init__(self):
        super().__init__()
        self.название = "Дары моря"
        self.тесто = "пышное"
        self.соус = "тар-тар"
        self.начинка = ["кальмары", "креветки", "мидии", "сыр моцарелла"]
        self.цена = 550


class Заказ:
    счетчик_заказов = 0

    def __init__(self):
        self.заказанные_пиццы = []
        Заказ.счетчик_заказов += 1
        self.номер = Заказ.счетчик_заказов

    def __str__(self):
        if not self.заказанные_пиццы:
            return f"Заказ №{self.номер} пуст."
        result = f"Заказ №{self.номер}\n"
        for i, пицца in enumerate(self.заказанные_пиццы, start=1):
            result += f"{i}. {пицца}\n"
        result += f"Сумма заказа: {self.сумма():.2f} р."
        return result

    def добавить(self, пицца):
        self.заказанные_пиццы.append(пицца)

    def сумма(self):
        return sum(пицца.цена for пицца in self.заказанные_пиццы)

    def выполнить(self):
        print("Заказ поступил на выполнение...")
        for пицца in self.заказанные_пиццы:
            print(f"{пицца.название}")
            пицца.подготовить()
            пицца.испечь()
            пицца.нарезать()
            пицца.упаковать()
        print(f"Заказ №{self.номер} готов! Приятного аппетита!")


class Терминал:
    КОМПАНИЯ = "Пиццерия #1"
    КОМАНДА_ОТМЕНА_ЗАКАЗА = -1
    КОМАНДА_ПОДТВЕРЖДЕНИЕ_ЗАКАЗА = 0

    def __init__(self):
        self.меню = [ПиццаПепперони(), ПиццаБарбекю(), ПиццаДарыМоря()]
        self.заказ = None
        self.отображать_меню = True

    def __str__(self):
        return f"{self.КОМПАНИЯ}\nДобро пожаловать!"

    def показать_меню(self):
        if not self.отображать_меню:
            return
        print(self)
        print("\nМеню:")
        for i, пицца in enumerate(self.меню, start=1):
            print(f"{i}. {пицца}")
        print("Для выбора укажите цифру через <ENTER>.")
        print(f"Для отмены заказа введите {self.КОМАНДА_ОТМЕНА_ЗАКАЗА}")
        print(f"Для подтверждения заказа введите {self.КОМАНДА_ПОДТВЕРЖДЕНИЕ_ЗАКАЗА}")
        self.отображать_меню = False

    def обработать_команду(self, пункт_меню):
        try:
            пункт_меню = int(пункт_меню)
            if пункт_меню == self.КОМАНДА_ОТМЕНА_ЗАКАЗА:
                self.заказ = None
                print("Заказ отменен.")
                self.отображать_меню = True
            elif пункт_меню == self.КОМАНДА_ПОДТВЕРЖДЕНИЕ_ЗАКАЗА:
                if not self.заказ:
                    print("Заказ пуст!")
                else:
                    print(self.заказ)
                    сумма = self.заказ.сумма()
                    print(f"Сумма заказа: {сумма:.2f} р.")
                    оплата = float(input("Введите сумму: "))
                    сдача = оплата - сумма
                    if сдача < 0:
                        print("Недостаточно средств для оплаты.")
                    else:
                        print(f"Вы внесли {оплата:.2f} р. Сдача: {сдача:.2f} р.")
                        self.заказ.выполнить()
                        self.заказ = None
                        self.отображать_меню = True
            elif 1 <= пункт_меню <= len(self.меню):
                if not self.заказ:
                    self.заказ = Заказ()
                выбранная_пицца = self.меню[пункт_меню - 1]
                self.заказ.добавить(выбранная_пицца)
                print(f"Пицца {выбранная_пицца.название} добавлена!")
            else:
                raise ValueError
        except ValueError:
            print("Не могу распознать команду! Проверьте ввод.")


if __name__ == "__main__":
    терминал = Терминал()
    print(терминал)
    while True:
        терминал.показать_меню()
        команда = input()
        терминал.обработать_команду(команда)
                   
