from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
import joblib

# dummy training data
X, y = make_regression(n_samples=100, n_features=4, noise=0.1)

# train model
model = RandomForestRegressor()
model.fit(X, y)

# save model
joblib.dump(model, "model.pkl")

print("model.pkl created successfully!")