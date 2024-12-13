import datetime

def get_first_monday():
    year = int(input("Введите год: "))
    week_number = int(input("Введите номер недели: "))
    
    first_day_of_year = datetime.date(year, 1, 1)
    days_to_add = (week_number - 1) * 7 - first_day_of_year.weekday()
    first_monday = first_day_of_year + datetime.timedelta(days=days_to_add)
    print(first_monday.strftime("пн %d %B %Y %H:%M:%S"))

if __name__ == "__main__":
    get_first_monday()
