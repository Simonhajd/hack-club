import datetime

today = datetime.date.today()
future = datetime.date(2024,8,31)
diff = future - today
print (diff.days)