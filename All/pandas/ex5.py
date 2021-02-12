#using Dictionaries

import pandas as p 
weather_data={
				'date':['18/06/2020','17/06/2020','24/02/2020'],
				'temperature':[37,29,25],
				'event':['sunny','moderate','rainy']
}
df=p.DataFrame(weather_data)
print(df)
print(type(df))


o/p:
----
#          date  temperature     event
# 0  18/06/2020           37     sunny
# 1  17/06/2020           29  moderate
# 2  24/02/2020           25     rainy
# <class 'pandas.core.frame.DataFrame'>