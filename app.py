!pip install -r requirements.txt
import streamlit as st
from PIL import Image
import io
import base64
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
# Set page configuration
icon_image_url = 'assets/logo.jpg'  # Replace with the URL of your icon image
st.set_page_config(page_title="HateDetect", layout="wide", page_icon=icon_image_url)

menu_options = ["Home", "Model","Meet Our  Team"]
selected = option_menu(menu_title=None, options=menu_options, orientation="horizontal")

# Define content for different sections based on the selected option
if selected == "Home":
    # Define content for the Home page
    st.title("About the Topic")

    # Left column with images
    col1, col2 = st.columns([1, 2])
    image_paths = ["assets/xx.jpg"]
    with col1:
        for image_path in image_paths:
            st.image(image_path, caption=f"Image {image_paths.index(image_path) + 1}", use_column_width=True)

    # Right column with text content
    with col2:
        st.markdown("""
        Hate speech is a form of communication, typically in the form of speech, writing, or behavior, that discriminates, degrades, or incites violence or prejudice against individuals or groups based on characteristics such as race, ethnicity, religion, gender, sexual orientation, disability, or other protected attributes. Hate speech is harmful for several reasons:

        - **Promotes Discrimination and Prejudice:** Hate speech perpetuates harmful stereotypes and biases, reinforcing discrimination against marginalized communities. It fosters an "us versus them" mentality and can lead to divisions and social conflicts.

        - **Threatens Safety:** Hate speech often includes threats and violent language, creating an atmosphere of fear and insecurity for targeted individuals or groups. It can escalate into real-life violence, harassment, or discrimination.

        - **Undermines Equality and Inclusion:** Hate speech hinders efforts to create inclusive and equal societies. It can discourage people from participating in public discourse, education, or the workplace, leading to social and economic disparities.

        - **Psychological Impact:** Exposure to hate speech can have significant psychological and emotional consequences, particularly for those who are targeted. It can lead to anxiety, depression, and feelings of isolation.

        - **Erodes Free Speech:** Paradoxically, hate speech can undermine the principles of free speech. When it goes unchecked, it can lead to censorship and restrictions on speech in an attempt to protect vulnerable populations.

        """)

        
        
if selected == "Model":
    # Load the dataset
    df = pd.read_csv('cleaned_data.csv')
    col1, col2 = st.columns(2)
    # Tokenization and padding
    with col1:
        max_words = 1000  # Adjust this value based on your dataset size
        max_sequence_length = 50  # Adjust based on your desired sequence length

        tokenizer = Tokenizer(num_words=max_words)
        tokenizer.fit_on_texts(df['post_tokens'])

        # Load the trained model
        loaded_model = load_model("your_model_name.h5")  # Replace with your model's file name

        # Streamlit app
        st.title("Test Our Model By Yourself")

        text = st.text_input("Enter a text to be classified:")
        if st.button("Predict"):
            sequence = tokenizer.texts_to_sequences([text])
            padded_sequence = pad_sequences(sequence, maxlen=max_sequence_length)
            prediction = loaded_model.predict(padded_sequence)

            if prediction[0][0] > 0.5:
                st.write("Predicted: hatespeech")
            else:
                st.write("Predicted: normal")
    with col2:
        st.image("assets/model_achi.jpg", caption="Model Architecture", use_column_width=True)
if selected=="Meet Our  Team":



    # Function to display team member information
    def display_team_member(image_filename, name, roll_number, email):
        st.markdown(
            f"## {name}",
            unsafe_allow_html=True
        )
        st.image(f"assets/{image_filename}")
        st.write(f"Roll Number: {roll_number}")
        st.write(f"Email: {email}")


    # Function to display mentor information
    def display_mentor(image_filename, name, linkedin_profile):
        st.markdown(f"## {name}", unsafe_allow_html=True)
        st.image(f"assets/{image_filename}")
        st.write(f"LinkedIn Profile: [{name}]({linkedin_profile})")








    col1, col2,col3,col4,col5 = st.columns(5)
    
    with col3:
        # Bolder text using HTML and CSS
        st.markdown("<p style='font-size: 34px; font-weight: bold; color: red;'>MENTOR</p>", unsafe_allow_html=True)
        # Example usage
        
        display_mentor("m.png", "Dr. Rupali Gangarde", "www.linkedin.com/in/dr-rupali-gangarde-33aa79121")

        
    col1, col2,col3,col4,col5 = st.columns(5)
    
    with col3:
        # Bolder text using HTML and CSS
        st.markdown("<p style='font-size: 40px; font-weight: bold; color: red;'>TEAM</p>", unsafe_allow_html=True)

        
    col1, col2, col3,col4,col5 = st.columns(5)
    
    # Display team members' information in each column
    with col2:
        display_team_member("1.png", "Moubani Ghosh", "20070122081", "moubani.ghosh.btech2020@sitpune.edu.in")

    with col3:
        display_team_member("2.png", "Ravi Thacker", "20070122108", "ravi.thacker.btech2020@sitpune.edu.in")

    with col4:
        display_team_member("3.png", "Rushali Tripathy", "20070124029", "rushali.tripathy.btech2020@sitpune.edu.in")
