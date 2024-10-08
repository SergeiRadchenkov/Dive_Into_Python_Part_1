'''
Напишите однострочный генератор словаря, 
который принимает на вход три списка одинаковой длины: 
имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
В результате получаем словарь с именем в качестве ключа 
и суммой премии в качестве значения. 
Сумма рассчитывается как ставка умноженная на процент премии
'''
import decimal

names = ['Valentin', 'Alexandra', 'Evgeni', 'Fekla']
salary = [50000, 75000, 180000, 150000]
bonus = ['50%', '26.6%', '10.8%', '22.14%']

print({name: salary_rate * round(float(bonus_rate.strip('%')) / 100, 2) 
    for name, salary_rate, bonus_rate in zip(names, salary, bonus)})
