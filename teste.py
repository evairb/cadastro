from datetime import datetime#, timezone
from pytz import timezone
import pytz
dt = datetime.now()
fuso = timezone('America/Sao_Paulo')
data = dt.astimezone(fuso)
dt_sp = data.strftime('%Y-%m-%d %H:%M:%S')
#
print(dt_sp)
#
#
#
#

#utc_dt = datetime.now(timezone.utc)
#
#
#data= (utc_dt)
#
#print(data)