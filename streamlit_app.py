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
def main():
    st.title('Bird Ecological Group Predictor')
    
    # Initialize an empty dictionary for features
    features = {}
    
    # Input section
    st.header('Input Features')
    huml = st.number_input('Humerus Length', min_value=0.0)
    humw = st.number_input('Humerus Width', min_value=0.0)
    ulnal = st.number_input('Ulna Length', min_value=0.0)
    ulnaw = st.number_input('Ulna Width', min_value=0.0)
    feml = st.number_input('Femur Length', min_value=0.0)
    femw = st.number_input('Femur Width', min_value=0.0)
    tibl = st.number_input('Tibiotarsus Length', min_value=0.0)
    tibw = st.number_input('Tibiotarsus Width', min_value=0.0)
    tarl = st.number_input('Tarsus Length', min_value=0.0)
    tarw = st.number_input('Tarsus Width', min_value=0.0)
    
    # Update the features dictionary
    features.update({
        'huml': huml,
        'humw': humw,
        'ulnal': ulnal,
        'ulnaw': ulnaw,
        'feml': feml,
        'femw': femw,
        'tibl': tibl,
        'tibw': tibw,
        'tarl': tarl,
        'tarw': tarw
    })
    
    # Predict button
    # Predict button
if st.button('Predict'):
    try:
        prediction = predict_ecological_group(features)
        
        # Output section
        st.header('Prediction Result')
        if prediction is not None:
            st.write(f'The predicted ecological group is: {prediction}')
        else:
            st.write("Prediction failed.")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")


if __name__ == '__main__':
    main()
