#using list of dictionaries

import pandas as p 
weather_data=[
				{'date':'18/06/2020','temperature':37,'event':'sunny'},
				{'date':'17/06/2020','temperature':29,'event':'moderate'},
				{'date':'24/02/2020','temperature':25,'event':'rainy'},			
]
df=p.DataFrame(weather_data)
print(df)
print(type(df))

# o/p:
# ----
#          date  temperature     event
# 0  18/06/2020           37     sunny
# 1  17/06/2020           29  moderate
# 2  24/02/2020           25     rainy
# <class 'pandas.core.frame.DataFrame'>

