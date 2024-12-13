import datetime

def add_years(date, years):
    try:
        new_date = date.replace(year=date.year + years)
    except ValueError:
        new_date = date.replace(year=date.year + years, day=28)
    return new_date

def get_new_date():
    year = int(input("Введите год: "))
    month = int(input("Введите месяц: "))
    day = int(input("Введите день: "))
    date = datetime.date(year, month, day)
    years_to_add = int(input("Введите количество лет: "))
    new_date = add_years(date, years_to_add)
    print(f"Новая дата: {new_date}")

if __name__ == "__main__":
    get_new_date()
