import time
from datetime import datetime, timezone, timedelta 


tz = timezone(timedelta(hours=+8))
# 取得現在時間、指定時區、轉為 ISO 格式
a = datetime.now(tz).isoformat()
#開始時間
print(datetime.strftime(a,"%Y/%m/%d %H:%M:%S"))

