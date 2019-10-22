# In this file, a pretrained model is loaded to calculate prices for used cars.

# Import Statements
import numpy as np
import pandas as pd
import pickle
from xgboost import XGBRegressor
from sklearn.preprocessing import scale
#import argparse

# Import model
filename = 'regressor.pkl'
loaded_regressor = pickle.load(open(filename, 'rb'))

# Import df_zips
df_zips = pickle.load(open('zips.pkl', 'rb'))

# Import columns for DataFrame
cols = pickle.load(open('df_cols.pkl', 'rb'))

# Create empty dataframe
#cols = ['vehicleType', 'automaticGear', 'powerPS', 'kilometer', 'fuelType', 'brand', 'notRepairedDamage', 'lon', 'lat', 'age']
data = np.zeros((1, len(cols)))
df_in = pd.DataFrame(columns=cols, data=data)
print(df_in)

# Parse input
print("Hello there, let's try to calculate the value of your car.")
print("Please input the vehicle type as one of the following choices: sedan, small, station, bus, convertible, coupe, suv, other.")
vehicleType_in = input().lower()
if vehicleType_in == 'sedan':
    vehicleType_in = 'limousine'
elif vehicleType_in == 'small':
    vehicleType_in = 'kleinwagen'
elif vehicleType_in == 'station':
    vehicleType_in = 'kombi'
vehicleType_in = 'vehicleType_' + vehicleType_in
df_in[vehicleType_in] = 1

print("Please enter the gearbox-type. 1 for automatic, 0 for manual.")
automaticGear_in = int(input())
df_in['automaticGear'] = automaticGear_in

print("Please enter the power in horsepowers [hp].")
powerPS_in = int(input())
df_in['powerPS'] = powerPS_in

print("Please enter the propulsion system as one of the following choices: gasoline, diesel, lpg, cng, hybrid, bev, other.")
fuelType_in = input().lower()
if fuelType_in == 'gasoline':
    fuelType_in = 'benzin'
elif fuelType_in == 'bev':
    fuelType_in = 'elektro'
elif fuelType_in == 'other':
    fuelType_in = 'andere'
fuelType_in = 'fuelType_' + fuelType_in
df_in[fuelType_in] = 1

print("Please enter the brand of the car.")
brand_in = 'brand_' + input().lower()
df_in[brand_in] = 1

print("Is there any unrepaired damage? If so, type 1, otherwise 0.")
notRepairedDamage = int(input())
df_in['notRepairedDamage'] = notRepairedDamage

print("Enter the age of the car in years.")
age_in = float(input())
df_in['age'] = age_in

print("And lastly: Please enter the (desired) location of the car as a german zip-code.")
zip_code_in = int(input())
lat_in = df_zips[df_zips['plz'] == zip_code_in].lat
lon_in = df_zips[df_zips['plz'] == zip_code_in].lon
city_in = df_zips[df_zips['plz'] == zip_code_in].Ort
df_in['lat'] = lat_in
df_in['lon'] = lon_in

print('Processing...')
print()

# Calculate price
y_pred = loaded_regressor.predict(df_in.values)
print('The predicted price for the entered car in {} is: {:.0f}€'.format(city_in.values[0], y_pred[0]))