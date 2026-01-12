import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


## 1: Load weather data set
# URL of the dataset on Zenodo
URL = 'https://zenodo.org/records/4770937/files/weather_prediction_dataset.csv'

#load the database into a Pandas DataFame
df = pd.read_csv(URL)

# Display the first few rows of dataset
print(df.head())

# Display basic info of the dataset
df.info()

# Display Summary statustics
print(df.describe())


print(df.isnull().sum())

# 1. Handle missing values
df = df.dropna()

# 2. convert categoricals into numbers: using One-hot encoding
df = pd.get_dummies(df, drop_first=True)

# 3. Feature Selection: Define features and target variables
X = df.drop('BASEL_temp_mean', axis = 1)
y = df['BASEL_temp_mean']


#Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Initialize the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)


# Make predictions
y_pred = model.predict(X_test)

# Calculate the Mean Squared Error (lower is better)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Calculate R-Squared Score (Percent)
r2 = r2_score(y_test, y_pred)
print(f'R-Squared Score: {r2}')


# plot actual vs predicted values
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs. Predicted Weather Conditions')
plt.show()