import datetime

def get_sundays():
    year = int(input("Введите год: "))
    sundays = []
    first_day_of_year = datetime.date(year, 1, 1)
    days_to_sunday = (6 - first_day_of_year.weekday()) % 7
    first_sunday = first_day_of_year + datetime.timedelta(days=days_to_sunday)
    current_sunday = first_sunday
    while current_sunday.year == year:
        sundays.append(current_sunday)
        current_sunday += datetime.timedelta(weeks=1)
    for sunday in sundays:
        print(sunday)

if __name__ == "__main__":
    get_sundays()
