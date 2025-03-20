# вывод рублей
def decline_ruble(n):

    if 11 <= n % 100 <= 19:
        return f"{n} рублей"
    last_digit = n % 10
    if last_digit == 1:
        return f"{n} рубль"
    elif 2 <= last_digit <= 4:
        return f"{n} рубля"
    else:
        return f"{n} рублей"


def dic_ruble(n):

    dic = {
        1: "рубль",
        2: "рубля",
        3: "рубля",
        4: "рубля",
        5: "рублей",
        6: "рублей",
        7: "рублей",
        8: "рублей",
        9: "рублей",
        0: "рублей",
    }

    if 11 <= n % 100 <= 19:
        return f"{n} {dic[0]}"

    else:
        return f"{n} {dic[n % 10]}"


num = int(input("Введите число: "))
print(decline_ruble(num))
print(dic_ruble(num))