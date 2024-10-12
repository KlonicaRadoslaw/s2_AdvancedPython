from datetime import datetime

def day_percentage():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    time_in_minutes = hour * 60 + minute + second / 60
    day_percentage = (time_in_minutes / 1440) * 100
    return now, day_percentage

def is_leap_year(year):
    if 1800 <= year <= 2200:
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    else:
        return "Rok musi byc pomiedzy 1800, a 2200"


def days_in_month(month, year):
    if month < 1 or month > 12:
        return "Miesiac musi byc pomiedzy 1, a 12."

    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_leap_year(year):
        return 29
    else:
        return days_in_months[month - 1]

if __name__ == '__main__':
    time_now, percent_minute = day_percentage()
    print(f"Aktualna data i czas: {time_now}")
    print(f"Procent dnia, który minął: {percent_minute:.2f}%")

    print(f"Czy 1900 to rok przestepny?: {is_leap_year(1900)}")
    print(f"Czy 2024 to rok przestepny?: {is_leap_year(2024)}")

    print(f"Liczba dni w pazdzierniku roku 2024: {days_in_month(10, 2024)}")
    print(f"Liczba dni w lutym roku 2024: {days_in_month(2, 2024)}")

