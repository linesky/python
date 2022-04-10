from datetime import datetime
from datetime import timedelta
t=datetime.now()	
t=t+timedelta(seconds=6)
t3=datetime.now()
while True:
	t1=datetime.now()
	if t1>t:
		break
print t3
print t
