# create data using faker
from faker import Faker
import pandas as pd
import random
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')


logging.warning('Watch out!')
logging.info('I told you so')

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
print(driver_profile.head())

## Create the vehicle profile

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
print(driver_profile.head())




