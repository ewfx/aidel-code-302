import pandas as pd
import joblib
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error

def load_model():
    
    # ✅ Load the dataset
    df = pd.read_csv("data/training_data.csv")

    # ✅ Define Features & Target
    features = ["Sender Predicted Category", "Receiver Predicted Category", "Sender Country", "Receiver Country"]
    df = df.dropna(subset=features + ["Risk Score"])  # Remove rows with missing values
    X = pd.get_dummies(df[features])  # Convert categorical features into numeric
    y = df["Risk Score"]

    # ✅ Split Data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # ✅ Define Hyperparameter Grid
    param_grid = {
        "n_estimators": [100, 200, 300],  # Number of trees
        "max_depth": [10, 20, None],  # Tree depth
        "min_samples_split": [2, 5, 10],  # Minimum samples to split a node
        "min_samples_leaf": [1, 2, 5],  # Minimum samples at a leaf node
        "max_features": ["sqrt", "log2"]  # Number of features per split
    }

    # ✅ Initialize RandomForestRegressor
    rf = RandomForestRegressor(random_state=42)

    # ✅ Perform Grid Search with 3-Fold Cross-Validation
    grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, 
                            scoring="neg_mean_squared_error", cv=3, n_jobs=-1, verbose=2)
    grid_search.fit(X_train, y_train)

    # ✅ Get Best Hyperparameters
    best_params = grid_search.best_params_
    print("Best Hyperparameters:", best_params)

    # ✅ Train Final Model with Best Parameters
    best_model = RandomForestRegressor(**best_params, random_state=42)
    best_model.fit(X_train, y_train)

    # ✅ Save the Best Model
    joblib.dump(best_model, "models/risk_score_model.pkl")
    print("Optimized Model trained and saved successfully!")

    # ✅ Evaluate Model Performance
    y_pred = best_model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print(f"Mean Absolute Error (MAE): {mae:.4f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
