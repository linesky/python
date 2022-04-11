from datetime import datetime
from datetime import timedelta
def sleeps(values):
	t=datetime.now()	
	t=t+timedelta(seconds=values)
	while True:
		t1=datetime.now()
		if t1>t:
			break
