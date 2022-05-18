def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")

greet()
arr = [[" "] * 3 for i in range(3)]
def array():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(arr):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()

array()


def ask():
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if arr[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


ask()
def check_win():
    win_numeric = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_numeric:
        symbols = []
        for c in cord:
            symbols.append(arr[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Поздравляем, выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Поздравляем, выиграл 0!!!")
            return True
    return False

arr = [
    [" ", "X", " "],
    [" ", "X", " "],
    [" ", "X", " "]
]

check_win()
greet()
arr = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    array()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        arr[x][y] = "X"
    else:
        arr[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break