import datetime

def time_difference():
    year1 = int(input("Введите год первой даты: "))
    month1 = int(input("Введите месяц первой даты: "))
    day1 = int(input("Введите день первой даты: "))
    hour1 = int(input("Введите час первой даты: "))
    minute1 = int(input("Введите минуту первой даты: "))
    second1 = int(input("Введите секунду первой даты: "))
    date1 = datetime.datetime(year1, month1, day1, hour1, minute1, second1)

    year2 = int(input("Введите год второй даты: "))
    month2 = int(input("Введите месяц второй даты: "))
    day2 = int(input("Введите день второй даты: "))
    hour2 = int(input("Введите час второй даты: "))
    minute2 = int(input("Введите минуту второй даты: "))
    second2 = int(input("Введите секунду второй даты: "))
    date2 = datetime.datetime(year2, month2, day2, hour2, minute2, second2)

    delta = date2 - date1
    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60

    print(f"Разница: {days} дней, {hours} часов, {minutes} минут, {seconds} секунд")

if __name__ == "__main__":
    time_difference()
