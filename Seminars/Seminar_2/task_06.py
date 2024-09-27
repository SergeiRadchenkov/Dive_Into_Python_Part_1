'''
Напишите программу банкомат.
* Начальная сумма равна нулю
* Допустимые действия: пополнить, снять, выйти
* Сумма пополнения и снятия кратны 50 у.е.
* Процент за снятие - 1,5% от суммы снятия, но не менее 30 и не более 600 у.е.
* После каждой третей операции пополнения или снятия начисляются проценты - 3%
* Нельзя снять больше, чем на счёте
* При превышении суммы в 5 млн, вычисляется налог на богатство 10% перед каждой операцией, даже ошибочной
* Любое действие выводит сумму денег
'''
import decimal

# decimal.getcontext().prec = 2
CMD_DEPOSIT = 'п'
CMD_WITHDRAW = 'с'
CMD_EXIT = 'в'
RICHNESS_SUM = decimal.Decimal(5_000_000 )
RICHNESS_TAX = decimal.Decimal(10) / decimal.Decimal(100)
WITHDRAW_PERCENT = decimal.Decimal(15) / decimal.Decimal(1000)
ADD_PERCENT = decimal.Decimal(3) / decimal.Decimal(100)
MULTIPLICITY = 50
MIN_RENOVAL = 30
MAX_RENOVAL = 600
COUNTER_OPER = 3

account = decimal.Decimal(0)
count = 0

while True:
    command = input(f'Пополнить - "{CMD_DEPOSIT}", Снять - "{CMD_WITHDRAW}", Выйти - "{CMD_EXIT}": ')
    if command == CMD_EXIT:
        print(f'Возьмите карту, на которой {account} у.е.')
        break
    if account > RICHNESS_SUM:
        percent = account * RICHNESS_TAX
        account -= percent
        print(f'Удержен налог на богатство в размере {percent} у.е.\n'
              f'Итого на карте осталось {account} у.е.')
    if command in (CMD_DEPOSIT, CMD_WITHDRAW):
        amount = 1
        while amount % 50 != 0:
            amount = int(input(f'Введите сумму, кратную {MULTIPLICITY}: '))
    if command == CMD_DEPOSIT:
        account += amount
        count += 1
        print(f'Пополнение карты на {amount} у.е.\nИтого на карте {account} у.е.')
    elif command == CMD_WITHDRAW:
        withdraw_tax = amount * WITHDRAW_PERCENT
        withdraw_tax = (MIN_RENOVAL if withdraw_tax < MIN_RENOVAL else 
                        MAX_RENOVAL if withdraw_tax > MAX_RENOVAL else withdraw_tax)
        if account >= amount + withdraw_tax:
            count += 1
            account -= (amount + withdraw_tax)
            print(f'Снятие с карты {amount} у.е.\nКомиссия за снятие {withdraw_tax} у.е.\n'
                  f'На карте осталось {account} у.е.')
        else:
            print(f'Недостаточное денег для выполнения операции\n'
                  f'Затребованная сумма {amount} у.е., Комиссия составила {withdraw_tax} у.е.\n'
                  f'На карте {account} у.е.')
    if count and count >= COUNTER_OPER:
        bonus_percent = account * ADD_PERCENT
        account += bonus_percent
        print(f'На счёт начислено {ADD_PERCENT}%, сущставляющие {bonus_percent} у.е.\n'
              f'Итого на карте {account} у.е.')