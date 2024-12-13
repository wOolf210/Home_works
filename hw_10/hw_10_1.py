import datetime

def get_week_number():
    year = int(input("Введите год: "))
    month = int(input("Введите месяц: "))
    day = int(input("Введите день: "))
    date = datetime.date(year, month, day)
    week_number = date.isocalendar()[1]
    print(f"Номер недели: {week_number}")

if __name__ == "__main__":
    get_week_number()
