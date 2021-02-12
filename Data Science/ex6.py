#using list of tuples

import pandas as p 
weather_data=[
				('18/06/2020',37,'sunny'),
				('17/06/2020',29,'moderate'),
				('24/02/2020',25,'rainy')
]
df=p.DataFrame(weather_data,columns=['date','temperature','event'])
print(df)
print(type(df))

# o/p:
# ----
#          date  temperature     event
# 0  18/06/2020           37     sunny
# 1  17/06/2020           29  moderate
# 2  24/02/2020           25     rainy
# <class 'pandas.core.frame.DataFrame'>