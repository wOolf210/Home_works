import calendar

def create_html_calendar():
    year = int(input("Введите год: "))
    month = int(input("Введите месяц: "))
    cal = calendar.HTMLCalendar(calendar.SUNDAY)
    html_calendar = cal.formatmonth(year, month)
    print(html_calendar)

if __name__ == "__main__":
    create_html_calendar()
