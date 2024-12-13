import datetime

def days_between_dates():
    year1 = int(input("Введите год первой даты: "))
    month1 = int(input("Введите месяц первой даты: "))
    day1 = int(input("Введите день первой даты: "))
    date1 = datetime.date(year1, month1, day1)

    year2 = int(input("Введите год второй даты: "))
    month2 = int(input("Введите месяц второй даты: "))
    day2 = int(input("Введите день второй даты: "))
    date2 = datetime.date(year2, month2, day2)

    delta = date2 - date1
    print(f"Количество дней между датами: {delta.days}")

if __name__ == "__main__":
    days_between_dates()
