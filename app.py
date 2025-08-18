# app.py

import streamlit as st
import pandas as pd
import joblib
from knowledge_base import get_recommendation
from rule_engine import get_rule_based_diagnosis

# --- Page Configuration ---
st.set_page_config(
    page_title="Maize Pest & Disease DSS",
    page_icon="🌽",
    layout="wide"
)

# --- Load Model and Encoder ---
@st.cache_resource
def load_assets():
    model = joblib.load('maize_dss_model.joblib')
    encoder = joblib.load('label_encoder.joblib')
    return model, encoder

model, label_encoder = load_assets()

# --- Application Header ---
st.title("DSS for Integrated Pest & Disease Management in Maize")
st.markdown("This system helps farmers in Imo State diagnose potential issues with their maize crop and receive sustainable management recommendations.")

# --- User Input Section ---
st.sidebar.header("Enter Crop and Environmental Data")

# Input widgets in the sidebar
temp = st.sidebar.slider("Average Temperature (°C)", 20, 40, 28)
humidity = st.sidebar.slider("Average Humidity (%)", 40, 100, 75)
rainfall = st.sidebar.slider("Recent Rainfall (mm)", 0, 50, 10)
crop_stage = st.sidebar.selectbox("Crop Growth Stage", ['Seedling', 'Vegetative', 'Flowering', 'Maturity'])

st.sidebar.subheader("Observed Symptoms")
# Use checkboxes for symptoms (1 if checked, 0 if not)
symptom_spots = st.sidebar.checkbox("Lesions or spots on leaves")
symptom_holes = st.sidebar.checkbox("Holes or 'shotgun' damage on leaves")
symptom_stunted = st.sidebar.checkbox("Stunted or poor plant growth")
symptom_wilting = st.sidebar.checkbox("Leaves are wilting or drying up")
symptom_boring = st.sidebar.checkbox("Signs of boring in the stem or cobs")

# --- Diagnosis Logic ---
if st.sidebar.button("Diagnose Crop", use_container_width=True):
    # 1. Collect user inputs into a dictionary
    user_data = {
        'Temperature': temp,
        'Humidity': humidity,
        'Rainfall_mm': rainfall,
        'Crop_Stage': crop_stage, # This will be handled for rule-based
        'Symptom_Leaf_Spots': int(symptom_spots),
        'Symptom_Holes_in_Leaves': int(symptom_holes),
        'Symptom_Stunted_Growth': int(symptom_stunted),
        'Symptom_Wilting': int(symptom_wilting),
        'Symptom_Stem_Boring': int(symptom_boring)
    }

    # 2. First, try the Rule-Based Engine
    rule_diagnosis = get_rule_based_diagnosis(user_data)
    final_diagnosis = "" # Initialize as a string
    source = ""

    if rule_diagnosis:
        final_diagnosis = rule_diagnosis
        source = "Rule-Based Engine (High Confidence)"
    else:
        # 3. If no rule matches, use the ML Model
        source = "Predictive Model (Machine Learning)"
        # Prepare data for the model (one-hot encoding)
        input_df = pd.DataFrame([user_data])
        # Manually create columns for one-hot encoding based on training
        all_crop_stages = ['Crop_Stage_Flowering', 'Crop_Stage_Maturity', 'Crop_Stage_Seedling', 'Crop_Stage_Vegetative']
        for stage_col in all_crop_stages:
            stage_name = stage_col.replace('Crop_Stage_', '')
            input_df[stage_col] = 1 if crop_stage == stage_name else 0
        
        # Remove original categorical column if it was accidentally included
        input_df = input_df.drop('Crop_Stage', axis=1, errors='ignore')
        
        # Ensure column order matches the training data
        training_cols = model.feature_names_in_
        input_df = input_df.reindex(columns=training_cols, fill_value=0)

        # Predict
        prediction = model.predict(input_df)
        
        # ==================== FIX IS HERE ====================
        # We extract the first item '[0]' to get the string from the numpy array
        final_diagnosis_array = label_encoder.inverse_transform(prediction)
        final_diagnosis = final_diagnosis_array[0]
        # =====================================================


    # --- Display Results ---
    st.header("Diagnosis Results")
    st.info(f"**Source of Diagnosis:** {source}")

    if final_diagnosis == 'Healthy':
        st.success(f"**Most Likely Status: {final_diagnosis}**")
    else:
        st.error(f"**Most Likely Issue: {final_diagnosis}**")

    # Get and display recommendations from the knowledge base
    recommendation = get_recommendation(final_diagnosis)

    st.subheader("Description")
    st.write(recommendation['description'])

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### Cultural Control")
        st.markdown(recommendation['cultural'])
    with col2:
        st.markdown("#### Biological Control")
        st.markdown(recommendation['biological'])
    with col3:
        st.markdown("#### Chemical Control")
        st.markdown(recommendation['chemical'])
else:
    st.info("Please enter the crop's data in the sidebar and click 'Diagnose Crop'.")