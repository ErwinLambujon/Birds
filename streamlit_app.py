import os
import joblib
import streamlit as st
import numpy as np

# Load the model
model_path = 'birds_classification.pkl'

# Check if the file exists
if os.path.exists(model_path):
    # Load the model
    try:
        model = joblib.load(model_path)
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Error loading the model: {e}")
else:
    print(f"Model file '{model_path}' does not exist.")

# Function to make predictions
def predict_ecological_group(input_data):
    try:
        # Convert input features dictionary to a NumPy array
        input_array = np.array(list(input_data.values())).reshape(1, -1)
        prediction = model.predict(input_array)
        return prediction[0]  # Return the first element of the prediction array
    except Exception as e:
        print(f"Error during prediction: {e}")
        return None

# Streamlit app
# Streamlit app
# Load the model (within the main function)
def main():
    # Initialize an empty dictionary for features
    features = {}

    # Load the model
    try:
        model = joblib.load(model_path)
        st.write("Model loaded successfully.")
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        return

    # Input section (same as before)

    # Predict button (same as before)

    if st.button('Predict'):
        try:
            prediction = predict_ecological_group(features, model)
            st.header('Prediction Result')
            if prediction is not None:
                st.write(f'The predicted ecological group is: {prediction}')
            else:
                st.write("Prediction failed.")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

# Function to make predictions (passing the model as an argument)
def predict_ecological_group(input_data, model):
    try:
        # Convert input features dictionary to a NumPy array
        input_array = np.array(list(input_data.values())).reshape(1, -1)
        prediction = model.predict(input_array)
        return prediction[0]  # Return the first element of the prediction array
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        return None

if __name__ == '__main__':
    main()
