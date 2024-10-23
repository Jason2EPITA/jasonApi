import streamlit as st
import joblib

# Load the saved regression model
model = joblib.load("regression.joblib")

# Input fields for user to input size, number of bedrooms, and garden status
size = st.number_input("Enter the size of the house (in square feet):", min_value=0.0, value=1000.0)
bedrooms = st.number_input("Enter the number of bedrooms:", min_value=1, value=3)
garden = st.number_input("Does the house have a garden? (0 for No, 1 for Yes):", min_value=0, max_value=1, value=1)

# Button to trigger prediction
if st.button("Predict Price"):
    # Arrange the input in the form that the model expects (as a 2D array)
    input_data = [[size, bedrooms, garden]]
    
    # Pass the input data to the model's predict method
    prediction = model.predict(input_data)
    
    # Display the prediction result
    st.write(f"The predicted house price is: ${prediction[0]:,.2f}")
