import streamlit as st
import joblib
import pandas as pd

st.title("Linear Regression")
st.subheader("Eurovision Final Place Predictor", divider='rainbow')

# Load trained model
@st.cache_resource
def load_model():
    return joblib.load('../Models/finalistfit.pkl') 

model = load_model()

def show_linear_regression():
    st.write("Enter the performance details below:")

    # Input fields for essential features
    year = st.number_input("Year", min_value=2000, max_value=2025, value=2023)
    draw_position = st.number_input("Final Draw Position", min_value=1, max_value=26, value=15)
    total_points = st.number_input("Total Points", min_value=0.0, value=250.0)

    # Input fields for optional features
    televote_points = st.number_input("Televote Points", min_value=0.0, value=150.0)
    jury_points = st.number_input("Jury Points", min_value=0.0, value=100.0)
    televote_votes = st.number_input("Televote Votes", min_value=0.0, value=100000.0)
    jury_votes = st.number_input("Jury Votes", min_value=0.0, value=50000.0)

    # Make prediction when button is pressed
    if st.button("Predict Final Place"):
        # Prepare input data as a DataFrame
        input_data = pd.DataFrame([[year, draw_position, televote_points, jury_points,
                                    televote_votes, jury_votes, total_points]],
                                  columns=['year', 'final_draw_position', 'final_televote_points', 
                                           'final_jury_points', 'final_televote_votes', 
                                           'final_jury_votes', 'final_total_points'])

        # Make prediction using the model
        prediction = model.predict(input_data)
        st.success(f"Predicted Final Place: {prediction[0]:.2f}")

# Run the function to display the interface
show_linear_regression()