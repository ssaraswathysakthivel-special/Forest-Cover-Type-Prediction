Forest Cover Type Prediction

Description:
This project predicts the forest cover type of a given area using machine learning.
It leverages topographic and environmental features such as elevation, slope, aspect, distances to hydrology, roadways, and fire points, as well as derived features like Aspect_sin, Elevation_Slope, and Hillshade_Mean.
The model is trained on historical forest data to classify each area into its corresponding cover type.
A Streamlit app allows interactive input of features via sliders for real-time predictions.

Technologies Used:
pandas, numpy for data manipulation
matplotlib, seaborn for visualization
scikit-learn for model training and evaluation
Streamlit for interactive web-based prediction

Project Approach

Data Loading and Exploration
Loaded forest cover dataset using pandas.
Explored distributions, missing values, and feature correlations.

Data Cleaning & Feature Engineering
Handled missing/inconsistent values.
Created derived features: Aspect_sin, Elevation_Slope, Hillshade_Mean, Hydrology_Distance, Hydrology_Ratio.
Standardized or scaled features for model training.

Feature Selection
Selected top features based on importance and correlation analysis.

Model Training
Split dataset into training/testing sets.
Trained a Random Forest Classifier with hyperparameter tuning.
Evaluated model using accuracy, cross-validation, and confusion matrix.

Model Saving
Saved trained model with joblib or pickle.
Saved label encoder for categorical target values.

Interactive Streamlit App

Built ranges for all relevant features.
Derived features computed dynamically from user input.
Predictions displayed in real-time.
Visualization & Insights
Plotted feature distributions, correlations, and feature importance.
Provided insights into environmental factors affecting forest cover.

