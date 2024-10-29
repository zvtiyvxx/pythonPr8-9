

def ceasar(text, shift):
    letters = [chr(i) for i in range(ord('а'), ord('я') + 1)]

    encoded = ""
    for char in text:
        if char in letters:
            new_pos = (letters.index(char) + shift) % len(letters)
            encoded += letters[new_pos]
        else:
            encoded += char

    decoded = ""
    for char in encoded:
        if char in letters:
            new_pos = (letters.index(char) - shift) % len(letters)
            decoded += letters[new_pos]
        else:
            decoded += char
    return encoded, decoded
try:
    text = str(input("Введите строку: "))
    shift = int(input("Введите сдвиг строки: "))
    if shift == 0:
        raise ZeroDivisionError("Сдвиг не может быть равен нулю")
except ValueError as e:
    print("Ошибка: Сдвиг не может быть строкой")
else:
    encoded, decoded = ceasar(text,shift)
    print("Зашифрованная строка:", encoded)
    print("Расшифрованная строка:", decoded)