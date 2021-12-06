from datetime import datetime
import pytz

bogota = pytz.timezone("America/Bogota")
#now recibe un objeto de tipo pytz
bogota_date = datetime.now(bogota)
print(bogota_date)

