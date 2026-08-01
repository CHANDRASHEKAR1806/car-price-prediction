import pandas as pd
import numpy as np
import joblib
import pickle
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv('data.csv')

# Feature columns
feature_cols = [
    'Engine HP', 'highway MPG', 'city mpg', 'Engine Cylinders', 
    'Number of Doors', 'Year', 'Popularity', 'Make', 
    'Engine Fuel Type', 'Transmission Type', 'Driven_Wheels', 
    'Vehicle Size', 'Vehicle Style'
]

# Impute missing values
for col in ['Engine HP', 'Engine Cylinders', 'Number of Doors']:
    df[col] = df[col].fillna(df[col].median())

for col in ['highway MPG', 'city mpg', 'Popularity', 'Year', 'MSRP']:
    df[col] = df[col].fillna(df[col].median())

# Encoding maps matching page 1 exactly
make_map = {
    "Acura": 0, "Alfa Romeo": 1, "Aston Martin": 2, "Audi": 3, "BMW": 4,
    "Bentley": 5, "Bugatti": 6, "Buick": 7, "Cadillac": 8, "Chevrolet": 9,
    "Chrysler": 10, "Dodge": 11, "FIAT": 12, "Ferrari": 13, "Ford": 14,
    "GMC": 15, "Genesis": 16, "HUMMER": 17, "Honda": 18, "Hyundai": 19,
    "Infiniti": 20, "Kia": 21, "Lamborghini": 22, "Land Rover": 23,
    "Lexus": 24, "Lincoln": 25, "Lotus": 26, "Maserati": 27, "Maybach": 28,
    "Mazda": 29, "McLaren": 30, "Mercedes-Benz": 31, "Mitsubishi": 32,
    "Nissan": 33, "Oldsmobile": 34, "Plymouth": 35, "Pontiac": 36,
    "Porsche": 37, "Rolls-Royce": 38, "Saab": 39, "Scion": 40, "Spyker": 41,
    "Subaru": 42, "Suzuki": 43, "Tesla": 44, "Toyota": 45, "Volkswagen": 46,
    "Volvo": 47
}
fuel_map = {"Regular Unleaded": 9, "Premium Unleaded (required)": 8, "Premium Unleaded (recommended)": 7, "Diesel": 0, "Electric": 1}
trans_map = {"Automatic": 1, "Manual": 3, "Automated Manual": 0, "Direct Drive": 2}
drive_map = {"Front Wheel Drive": 2, "Rear Wheel Drive": 3, "All Wheel Drive": 0, "Four Wheel Drive": 1}
size_map = {"Compact": 0, "Midsize": 2, "Large": 1}
style_map = {"Sedan": 14, "Coupe": 8, "4dr SUV": 3, "Convertible": 6, "2dr Hatchback": 0, "Crew Cab Pickup": 9}

# Apply encodings
le = LabelEncoder()
for c in ['Make', 'Engine Fuel Type', 'Transmission Type', 'Driven_Wheels', 'Vehicle Size', 'Vehicle Style']:
    df[c] = le.fit_transform(df[c].astype(str))

X = df[feature_cols].values
y = df['MSRP'].values

# Fit Gradient Boosting Regressor
gbm = GradientBoostingRegressor(n_estimators=120, max_depth=6, random_state=42)
gbm.fit(X, y)

print(f"Model R2 Score on full dataset: {gbm.score(X, y):.4f}")

# Save with pickle protocol=4 for maximum cross-version compatibility
with open('car_price_gradient_boosting.pkl', 'wb') as f:
    pickle.dump(gbm, f, protocol=4)

print("Saved car_price_gradient_boosting.pkl successfully!")