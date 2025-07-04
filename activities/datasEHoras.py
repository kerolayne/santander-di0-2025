import datetime

d = datetime.datetime(2025,6,23, 15, 30, 45)
print(d)
print(d.strftime("%d/%m/%Y %H:%M:%S"))

d = d + datetime.timedelta(days=5, hours=2, minutes=30)
print(d)
print(d.strftime("%d/%m/%Y %H:%M:%S"))

#trabalahndo com timezone
import pytz

# Definindo um fuso horário
fuso_horario = pytz.timezone("America/Sao_Paulo")

# Aplicando o fuso horário ao objeto datetime
d = fuso_horario.localize(d)
print(d)
print(d.strftime("%d/%m/%Y %H:%M:%S"))

# Convertendo para outro fuso horário
d_utc = d.astimezone(pytz.utc)
print(d_utc)
print(d_utc.strftime("%d/%m/%Y %H:%M:%S"))