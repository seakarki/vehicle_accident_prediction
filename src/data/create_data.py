# create data using faker
from faker import Faker
import pandas as pd
import random



import logging
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.debug('This is a log message.')

faker = Faker()

## Create the driver profile
driver_name = [faker.name() for i in range(1000)]
driver_age = [random.randint(18,60) for i in range(1000)]
driver_alcholic = [random.choice(['yes','no']) for i in range(1000)]
driver_has_kids =[random.choice(['yes','no']) for i in range(1000)]
driver_marital_status =[random.choice(['S','M']) for i in range(1000)]
driver_ownership =[random.choice(['yes','no']) for i in range(1000)]
driver_license_age= [random.randint(2,25) for i  in range(1000)]

columns = ['driver_name','driver_age','is_driver_alcholic','is_driver_has_kids',
           'driver_marital_status','driver_ownership','driver_license_age']

driver_profile = pd.DataFrame(list(zip(driver_name,
                               driver_age,
                               driver_alcholic,
                               driver_has_kids,
                               driver_marital_status,
                               driver_ownership,
                               driver_license_age)),columns=columns)
print("The datasets for driver: \n", driver_profile.head())


## Create the vehicle profile

vehicle_year = [random.randint(2000,2020) for i in range(1000)]
vehicle_age = [random.randint(1,25) for i in range(1000)]
vehicle_mileage = [random.randint(5000,300000) for i in range(1000)]
vehicle_last_maintaince = [random.randint(2015,2020) for i in range(1000)]

columns = ['vehicle_year','vehicle_age','vehicle_mileage','vehicle_last_maintaince']

vehicle_profile = pd.DataFrame(list(zip(vehicle_year,
                               vehicle_age,
                               vehicle_mileage,
                               vehicle_last_maintaince)),columns=columns)
print("The datasets for vehicle: \n", vehicle_profile.head())


## Create the road profile

road_condition = [random.choice(['pitch','gravel','off_road']) for i in range(1000)]
season = [random.choice(['rainy','winter','summer','autumn']) for i in range(1000)]
road_terrain = [random.choice(['hilly','mountain','terai']) for i in range(1000)]
day = [random.randint(1,29) for i in range(1000)]

month= [random.randint(1,12) for i in range(1000)]


columns = ['road_condition','season','road_terrain','day','month']
road_profile = pd.DataFrame(list(zip(road_condition,season,road_terrain,day,month)),columns=columns)

print("The datasets for road: \n", road_profile.head())

### Combine three datasets  together

driver_vehicle_road_df = pd.concat([driver_profile,vehicle_profile,road_profile],axis = 1)
print("The final datasets:\n",driver_vehicle_road_df.head())

## save the final datasets as csv
driver_vehicle_road_df.to_csv(
    "/Users/ocean/PycharmProjects/vehicle_accident_prediction/data/driver_vehicle_road_df.csv",index=False)


