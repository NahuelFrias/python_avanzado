from datetime import datetime

#tiempo exacto con microsegundos
#deberia utilizar .utcnow para obtener la fecha de donde se utilice mi app
my_time = datetime.now()
print(my_time)

#fecha dia mes año formato LATAM
my_day = my_time.strftime('%d/%m/%Y')
print(my_day)