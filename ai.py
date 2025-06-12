import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data={
    "Square-Footage":[650,800,1200,1500,2000],
    "Price":[20000,250000, 300000, 350000, 500000]
}

df=pd.DataFrame(data);
print(df)

X = df[["Square-Footage"]]  # Input feature
y = df["Price"]  # Target variable

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model=LinearRegression()
model.fit(X_train,y_train)

print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_)

y_pred = model.predict(X_test)

print("Actual Prices:", list(y_test))
print("Predicted Prices:", list(y_pred))

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

plt.scatter(X, y, color="blue", label="Actual Data")

plt.plot(X, model.predict(X), color="red", label="Regression Line")

plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.title("Linear Regression - House Prices")
plt.legend()
plt.savefig("regression_plot.png")
print("Plot saved as regression_plot.png")