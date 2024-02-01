import streamlit as st
import pandas as pd
import joblib
from utils import preprocessor

custom_css = """
    <style>
        body {
            background-color: #f0f0f0; /* Set your desired background color */
            font-family: 'Arial', sans-serif; /* Set your desired font */
        }
        .stApp {
            color: #333; /* Set your desired text color */
        }
        .stTextInput, .stSelectbox, .stTextArea {
            background-color: #ffffff; /* Set the background color for input elements */
            color: #333; /* Set the text color for input elements */
        }
        .stButton {
            background-color: #4CAF50; /* Set your desired button color */
            color: #ffffff; /* Set the text color for buttons */
        }
        /* Add more CSS styles as needed */
    </style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Your Streamlit app content goes here
st.title("Customized Streamlit App")
st.text("This is a sample Streamlit app with a custom color pattern.")

def run():





    model = joblib.load(open('model.joblib','rb'))

    st.title("Sentiment Analysis")
    st.text("Basic app to detect the sentiment of text.")
    st.text("")
    userinput = st.text_input('Enter text below, then click the Predict button.', placeholder='Input text HERE')
    st.text("")
    predicted_sentiment = ""
    if st.button("Predict"):
        predicted_sentiment = model.predict(pd.Series(userinput))
        if predicted_sentiment == 1:
            output = 'positive 👍'
        else:
            output = 'negative 👎'
        sentiment=f'Predicted sentiment of "{userinput}" is {output}.'
        st.success(sentiment)

if __name__ == "__main__":
    run()