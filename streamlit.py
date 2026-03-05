import streamlit as st
import numpy as np
import pandas as pd
from joblib import load

# -------------------------------
# Load Saved Model
# -------------------------------
model = load(r'C:\Users\ADMIN\Documents\mini_project_guvi\project_ecotype\final_cover_type_model.joblib')

# -------------------------------
# Page Title
# -------------------------------
st.set_page_config (page_title="Forest Cover Type Prediction", layout="wide")


st.markdown(
    """
    <div style="
        background: linear-gradient(90deg, #ff6b6b, #4ecdc4);
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 10px;
    ">
        <h1 style="color:#111; font-size:2.5rem; margin:0;">
            🌲 Forest Cover Type Prediction
        </h1>
        
    </div>
    """,
    unsafe_allow_html=True
)

st.caption(":blue[Enter environmental features to predict the forest cover type]")

# -------------------------------
# Helper function to get numeric midpoint from range string
# -------------------------------
def get_midpoint(range_str):
    """Convert a string 'min:max' to numeric midpoint"""
    low, high = map(float, range_str.split(':'))
    return (low + high)/2

# -------------------------------
# Define ranges for all numeric columns
# -------------------------------
elevation_ranges = ["0:500", "500:1000", "1000:1500", "1500:2000", "2000:2500"]
slope_ranges = ["0:10","10:20","20:30","30:40","40:50","50:60"]
dist_ranges = ["0:50","50:100","100:500","500:1000","1000:5000"]
hydro_ratio_ranges = ["0:0.2","0.2:0.4","0.4:0.6","0.6:0.8","0.8:1.0"]
hillshade_ranges = ["0:50","50:100","100:150","150:200","200:255"]
aspect_sin_ranges = ["-1.0:-0.5","-0.5:0","0:0.5","0.5:1.0"]
elevation_slope_ranges = ["0:500","500:1000","1000:1500","1500:2000","2000:2500"]
vertical_dist_ranges = ["-500:-250","-250:0","0:250","250:500"]

# -------------------------------
# Layout with 5 columns (priority order)
# -------------------------------
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    Elevation = get_midpoint(st.selectbox("Elevation (m)", elevation_ranges))
    Horizontal_Distance_To_Roadways = get_midpoint(st.selectbox("Distance To Roadways (m)", dist_ranges))
    Horizontal_Distance_To_Fire_Points = get_midpoint(st.selectbox("Distance To Fire Points (m)", dist_ranges))
    Hydrology_Distance = get_midpoint(st.selectbox("Hydrology Distance (m)", dist_ranges))

with col2:
    Hydrology_Ratio = get_midpoint(st.selectbox("Hydrology Ratio", hydro_ratio_ranges))
    Horizontal_Distance_To_Hydrology = get_midpoint(st.selectbox("Distance To Hydrology (m)", dist_ranges))
    Vertical_Distance_To_Hydrology = get_midpoint(st.selectbox("Vertical Distance (m)", vertical_dist_ranges))
    Aspect_sin = get_midpoint(st.selectbox("Aspect sin", aspect_sin_ranges))

with col3:
    Elevation_Slope = get_midpoint(st.selectbox("Elevation Slope (m)", elevation_slope_ranges))
    Hillshade_Mean = get_midpoint(st.selectbox("Hillshade Mean", hillshade_ranges))

with col4:
    Hillshade_Noon = get_midpoint(st.selectbox("Hillshade Noon", hillshade_ranges))
    Hillshade_3pm = get_midpoint(st.selectbox("Hillshade 3pm", hillshade_ranges))
    Hillshade_9am = get_midpoint(st.selectbox("Hillshade 9am", hillshade_ranges))

with col5:
    Slope = get_midpoint(st.selectbox("Slope (°)", slope_ranges))

# -------------------------------
# Soil Type Dropdown
# -------------------------------
Soil_Type = st.selectbox("Soil Type", 
                         ["Soil_Type_12.0", "Soil_Type_10.0", 
                          "Soil_Type_29.0", "Soil_Type_3.0",
                          "Soil_Type_23.0", "Soil_Type_30.0"])

# -------------------------------
# Prediction Button
# -------------------------------
if st.button("Predict Cover Type"):

    # One-hot encode soil type
    soil_columns = ["Soil_Type_12.0","Soil_Type_10.0","Soil_Type_29.0",
                    "Soil_Type_3.0","Soil_Type_23.0","Soil_Type_30.0"]
    soil_values = [1 if col==Soil_Type else 0 for col in soil_columns]

    # Prepare input array in correct column order
    input_data = np.array([[Elevation,
                            Horizontal_Distance_To_Roadways,
                            Horizontal_Distance_To_Fire_Points,
                            Hydrology_Distance,
                            Hydrology_Ratio,
                            Horizontal_Distance_To_Hydrology,
                            Vertical_Distance_To_Hydrology,
                            Aspect_sin,
                            Elevation_Slope,
                            Hillshade_Mean,
                            Hillshade_Noon,
                            Hillshade_3pm,
                            Hillshade_9am,
                            Slope,
                            *soil_values]])

    # Scale input if your model used a scaler
    # input_data = scaler.transform(input_data)

    # Predict single cover type
    prediction = model.predict(input_data)[0]

    # Map numeric prediction to forest cover type
    cover_mapping = {
        0: "Spruce/Fir",
        1: "Lodgepole Pine",
        2: "Ponderosa Pine",
        3: "Cottonwood/Willow",
        4: "Aspen",
        5: "Douglas-fir",
        6: "Krummholz"
    }

    st.success(f"Predicted Forest Cover Type: 🌳 {cover_mapping[prediction]}")