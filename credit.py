from datetime import datetime, timedelta

def print_next_month(date):
    date_obj = datetime.strptime(date, "%Y-%m-%d")     # Преобразуем строку с датой в объект datetime
    next_month = date_obj + timedelta(days=31)         # прибавляем месяц
    return next_month.strftime("%Y-%m-%d")

def credit_calculator(summ, percent, period, date):     # функция для расчета выплат и добавления ее в список

    if summ >= 0 and percent >= 0 and period >= 0:
        enterDict = {}

        for i in range(1, period + 1):
            payment = (summ / period) + ((summ - (summ / period) * (i - 1)) / 100) * (percent / 12)
            enterDict[print_next_month(date)] = summ, percent, period, round(payment, 2)
            date = print_next_month(date)
        
        return enterDict
    else:
        raise ValueError

try:                                                    # вводим данные о кредите
    summ = float(input("enter summ:"))
    percent = float(input("enter percent:"))               
    period = int(input("enter period:"))
    date = str(input("enter date:"))

    print(credit_calculator(summ, percent, period, date))

except ValueError:
    print("введите все в цифрах!")
except KeyboardInterrupt:
    print("вы завершили программу!")
except:
    print("возникла какая-то ошибка!")