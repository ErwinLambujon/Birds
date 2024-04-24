import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('birds_classificatio.pkl')

# Function to make predictions
def predict_ecological_group(features):
    # Assuming 'features' is a dictionary containing input values
    input_data = pd.DataFrame([features])
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit app
def main():
    st.title('Bird Ecological Group Predictor')
    
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
    
    # Predict button
    if st.button('Predict'):
        features = {
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
        }
        prediction = predict_ecological_group(features)
        
        # Output section
        st.header('Prediction Result')
        st.write(f'The predicted ecological group is: {prediction}')

if __name__ == '__main__':
    main()
