import time

arr = [
    [" ", "0", "1", "2"],
    ["0", "-", "-", "-"],
    ["1", "-", "-", "-"],
    ["2", "-", "-", "-"]
]
res = ""
def print_table():
    for i in range(4):
        print(" ".join(str(elem) for elem in arr[i]))

def check_table(text="Продолжаем играть дальше!"):
    global res
    if all(i == "X" for i in arr[1][1:]) \
      or all(i == "X" for i in arr[2][1:]) \
      or all(i == "X" for i in arr[3][1:])  \
      or (arr[1][1] == "X" and arr[2][1] == "X" and arr[3][1] == "X") \
      or (arr[1][2] == "X" and arr[2][2] == "X" and arr[3][2] == "X") \
      or (arr[1][3] == "X" and arr[2][3] == "X" and arr[3][3] == "X") \
      or (arr[1][1] == "X" and arr[2][2] == "X" and arr[3][3] == "X") \
      or (arr[3][1] == "X" and arr[2][2] == "X" and arr[1][3] == "X"):
        res = "Победитель игрок №1! "
        print(res * 3)

    elif all(i == "O" for i in arr[1][1:]) \
      or all(i == "O" for i in arr[2][1:]) \
      or all(i == "O" for i in arr[3][1:])  \
      or (arr[1][1] == "O" and arr[2][1] == "O" and arr[3][1] == "O") \
      or (arr[1][2] == "O" and arr[2][2] == "O" and arr[3][2] == "O") \
      or (arr[1][3] == "O" and arr[2][3] == "O" and arr[3][3] == "O") \
      or (arr[1][1] == "O" and arr[2][2] == "O" and arr[3][3] == "O") \
      or (arr[3][1] == "O" and arr[2][2] == "O" and arr[1][3] == "O"):
        res = "Победитель игрок №2! "
        print(res * 3)

    elif not any(i == "-" for i in arr[1][1:]) \
      and not any(i == "-" for i in arr[2][1:]) \
      and not any(i == "-" for i in arr[3][1:]):
        res = "Ничья! "
        print(res * 3)

    else:
        print(text)
        time.sleep(2)

def input_data(s, name_player):
    while True:
        player = (input("Введите координаты \"" + s + "\" через пробел, играет " + name_player + ": ")).strip()
        if player[0].isdigit():
            if int(player[0]) or int(player[0]) == 0:
                x = int(player[0])
            else:
                print("Введите число от 0 до 2 включительно! Скорее всего ввели отрицательное число")
                continue
        else:
            print("Введите число от 0 до 2 включительно! Скорее всего ввели не цифру!")
            continue
        if player[-1].isdigit():
            if int(player[-1]) or int(player[-1]) == 0:
                y = int(player[-1])
            else:
                print("Введите число от 0 до 2 включительно! Скорее всего ввели отрицательное число")
                continue
        else:
            print("Введите число от 0 до 2 включительно! Скорее всего ввели не цифру!")
            continue
        if not(0 <= x < 3 and 0 <= y < 3):
            print("Вы ввели неправильные координаты! Координаты лежат в диапозоне от 0 до 2 включительно!")
            continue
        if arr[x + 1][y + 1] == "-":
            arr[x + 1][y + 1] = s
            break
        else:
            print("Данная позиция уже занята!")
            continue

check_table("Начинаем игру!")
print("***********************")
print_table()

while True:
    input_data("X", "игрок №1")
    print_table()
    check_table()
    if res == "Победитель игрок №1! " or res == "Победитель игрок №2! " or res == "Ничья! ":
        break
    input_data("O", "игрок №2")
    print_table()
    check_table()
    if res == "Победитель игрок №1! " or res == "Победитель игрок №2! " or res == "Ничья! ":
        break