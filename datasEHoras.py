import datetime

d = datetime.datetime(2025,6,23, 15, 30, 45)
print(d)
print(d.strftime("%d/%m/%Y %H:%M:%S"))

d = d + datetime.timedelta(days=5, hours=2, minutes=30)
print(d)
print(d.strftime("%d/%m/%Y %H:%M:%S"))