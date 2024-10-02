'''
Возьмите задачу о банкомате из семинара 2. 
Разбейте её на отдельные операции — функции. 
Дополнительно сохраняйте все операции поступления и снятия средств в список.
'''

import decimal

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
list_of_commands = []


def deposit():
    global account, count
    if account > RICHNESS_SUM:
        percent = account * RICHNESS_TAX
        account -= percent
        print(f'Удержен налог на богатство в размере {percent} у.е.\n'
            f'Итого на карте осталось {account:.2f} у.е.')
        list_of_commands.append(f'Удержен налог на богатство в размере {percent} у.е.')
        list_of_commands.append(f'Итого на карте осталось {account:.2f} у.е.')
    amount = 1
    while amount % 50 != 0:
        amount = int(input(f'Введите сумму, кратную {MULTIPLICITY}: '))
    account += amount
    count += 1
    print(f'Пополнение карты на {amount} у.е.\nИтого на карте {account:.2f} у.е.')
    list_of_commands.append(f'Пополнение карты на {amount} у.е.')
    list_of_commands.append(f'Итого на карте {account:.2f} у.е.')
    if count and count >= COUNTER_OPER:
        bonus_percent = account * ADD_PERCENT
        account += bonus_percent
        print(f'На счёт начислено {ADD_PERCENT}%, равной {bonus_percent} у.е.\n'
            f'Итого на карте {account:.2f} у.е.')
        list_of_commands.append(f'На счёт начислено {ADD_PERCENT}%, равной {bonus_percent} у.е.')
        list_of_commands.append(f'Итого на карте {account:.2f} у.е.')
            

def withdraw():
    global account, count
    if account > RICHNESS_SUM:
        percent = account * RICHNESS_TAX
        account -= percent
        print(f'Удержен налог на богатство в размере {percent} у.е.\n'
            f'Итого на карте осталось {account:.2f} у.е.')
        list_of_commands.append(f'Удержен налог на богатство в размере {percent} у.е.')
        list_of_commands.append(f'Итого на карте осталось {account:.2f} у.е.')
    amount = 1
    while amount % 50 != 0:
        amount = int(input(f'Введите сумму, кратную {MULTIPLICITY}: '))
    withdraw_tax = amount * WITHDRAW_PERCENT
    withdraw_tax = (MIN_RENOVAL if withdraw_tax < MIN_RENOVAL else 
                    MAX_RENOVAL if withdraw_tax > MAX_RENOVAL else withdraw_tax)
    if account >= amount + withdraw_tax:
        count += 1
        account -= (amount + withdraw_tax)
        print(f'Снятие с карты {amount} у.е.\nКомиссия за снятие {withdraw_tax} у.е.\n'
            f'На карте осталось {account:.2f} у.е.')
        list_of_commands.append(f'Снятие с карты {amount} у.е.')
        list_of_commands.append(f'Комиссия за снятие {withdraw_tax} у.е.')
        list_of_commands.append(f'Итого на карте осталось {account:.2f} у.е.')
    else:
        print(f'Недостаточное денег для выполнения операции\n'
            f'Затребованная сумма {amount} у.е., Комиссия составила {withdraw_tax} у.е.\n'
            f'На карте {account:.2f} у.е.')
        list_of_commands.append(f'Недостаточное денег для выполнения операции')
        list_of_commands.append(f'Затребованная сумма {amount} у.е., Комиссия составила {withdraw_tax} у.е.')
        list_of_commands.append(f'На карте {account:.2f} у.е.')
    if count and count >= COUNTER_OPER:
        bonus_percent = account * ADD_PERCENT
        account += bonus_percent
        print(f'На счёт начислено {ADD_PERCENT}%, сущставляющие {bonus_percent} у.е.\n'
            f'Итого на карте {account:.2f} у.е.')
        list_of_commands.append(f'На счёт начислено {ADD_PERCENT}%, равной {bonus_percent} у.е.')
        list_of_commands.append(f'Итого на карте {account:.2f} у.е.')
        

def exit():
    global account
    if account > RICHNESS_SUM:
        percent = account * RICHNESS_TAX
        account -= percent
        print(f'Удержен налог на богатство в размере {percent} у.е.\n'
            f'Итого на карте осталось {account:.2f} у.е.')
        list_of_commands.append(f'Удержен налог на богатство в размере {percent} у.е.')
        list_of_commands.append(f'Итого на карте осталось {account:.2f} у.е.')
    print(f'Возьмите карту, на которой {account:.2f} у.е.')


def menu():
    while True:
        command = input(f"Выберите команду: \n\t{CMD_DEPOSIT} - пополнение \n\t{CMD_WITHDRAW} - снятие \n\t{CMD_EXIT} - выход \n: ").lower()
        if command == CMD_DEPOSIT:
            deposit()
        elif command == CMD_WITHDRAW:
            withdraw()
        elif command == CMD_EXIT:
            exit()
            break
        else:
            print('Некорректная команда.')
            print() 


menu()

print('Список всех выполненных операций: ')
for i in list_of_commands:
    print(i)
