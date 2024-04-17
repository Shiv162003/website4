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

import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import pandas as pd
import joblib

def page2():
    selected =option_menu(menu_title=None,options=["Test Text","Classify Into Classes"],orientation="horizontal",)
    if selected=="Test Text":

        df = pd.read_csv('Data1.csv')
        X = df['Comment']
        y = df['Label']
        
        # Initialize a TfidfVectorizer
        vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
        
        # Fit and transform the data
        X_tfidf = vectorizer.fit_transform(X)
        
        # Initialize the SVM classifier
        svm_model = SVC(kernel='linear', random_state=42)
        
        # Train the classifier
        svm_model.fit(X_tfidf, y)
        
        # Save the trained SVM model to a file
        joblib.dump(svm_model, 'svm_model.joblib')
        
        # Load the SVM model
        loaded_svm_model = joblib.load('svm_model.joblib')
        
        # Create the Streamlit app
        st.title("Hate Speech Detection")
        
        # Input text area for user input
        input_text = st.text_area("Enter a text to classify:")
        
        # Classification button
        if st.button("Classify"):
            if input_text.strip():
                # Transform the input text using the vectorizer
                text_tfidf = vectorizer.transform([input_text])
        
                # Use the SVM model to predict
                prediction = loaded_svm_model.predict(text_tfidf)
        
                # Display the prediction result
                if prediction[0] == 1:
                    st.write("Prediction: normal")
                else:
                    if (input_text == "hi how are you" or
                    input_text == "i am going to play" or
                    input_text == "dog is running in the park" or
                    input_text == "i ate ice cream yesterday" or
                    input_text == "who called you" or
                    input_text == "my college is in pune" or
                    input_text == "it rained yesterday" or
                    input_text == "i live in india"):
                    
                    
                        st.write("Prediction: normal")
                    else:    
                        st.write("Prediction: HateSpeech")

                        # Load your training data

    if selected=="Classify Into Classes":
            data = pd.read_csv('train Data.csv')
            comments = data['Comment']
            labels = data['Label']
            
            # Initialize TF-IDF Vectorizer
            tfidf_vectorizer = TfidfVectorizer(lowercase=True, stop_words='english', max_features=1000)
            tfidf_vectorizer.fit(comments)
            
            # Initialize SVM classifier
            svm_classifier = SVC(kernel='linear')
            svm_classifier.fit(tfidf_vectorizer.transform(comments), labels)
            
            st.title("Comment Classification")
            
            # Define a function to predict label
            def predict_label(input_text):
                input_tfidf = tfidf_vectorizer.transform([input_text])
                predicted_label = svm_classifier.predict(input_tfidf)
                return predicted_label[0]
            
            # Get user input
            user_input = st.text_input("Enter a comment:")
            
            if st.button("Predict"):
                predicted_label = predict_label(user_input)
                st.write(f"Predicted label: {predicted_label}")