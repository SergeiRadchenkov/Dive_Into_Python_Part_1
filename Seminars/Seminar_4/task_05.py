'''
✔ Функция принимает на вход три списка одинаковой длины:
    ✔ имена str,
    ✔ ставка int,
    ✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии.
'''
import decimal


def list_of_bounses(names: list[str], bets: list[int], rewards: list[str]) -> dict[str, decimal.Decimal]:
    result = {}
    for names, bets, rewards in zip(names, bets, rewards):
    # for i in range(len(names)):
        result[names] = bets * decimal.Decimal(rewards[:-1]) / 100
        # result[names[i]] = bets[i] * decimal.Decimal(rewards[i][:-1]) / 100
    return result



n = ['Alex', 'Ben', 'Chris']
b = [20000, 10000, 30000]
r = ['5.5%', '10.25%', '3.14%']
print(list_of_bounses(n, b, r))
