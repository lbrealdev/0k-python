from datetime import datetime, timedelta

now = datetime.now()

first_day_week = now - timedelta(days=now.weekday())

currently_day = int(now.strftime("%d"))
currently_month = int(now.strftime("%m"))
currently_year = int(now.strftime("%Y"))

current_date = datetime(currently_year, currently_month, currently_day)

_date = now.strftime("%d-%m-%Y")
_time = now.strftime("%H:%M:%S")
week_number_iso = current_date.isocalendar()[1]
week_number_sunday = current_date.strftime("%U")
week_number_monday = current_date.strftime("%W")
year = current_date.strftime("%Y")
month = current_date.strftime("%m")
day = current_date.strftime("%j")
week = current_date.strftime("%A")
satuday = first_day_week + timedelta(days=5)
sunday = first_day_week + timedelta(days=6)

print()
print()
print(f"Currenty date: {_date}")
print(f"Currenty time: {_time}")
print(f"Week number [ISO format]: {week_number_iso}")
print(f"Week number [starts on Sunday]: {week_number_sunday}")
print(f"Week number [starts on Monday]: {week_number_monday}")
print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day of the year: {day}")
print(f"Currently day of the week: {week}")
print(f"Saturday of the currently week: {satuday.strftime('%Y-%m-%d')}")
print(f"Sunday of the currently week: {sunday.strftime('%Y-%m-%d')}")
print()
print()

