import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from module import page2
import os
def main():
    st.set_page_config(page_title="FemGuard", page_icon=Image.open("assets/logo.jpg"), layout="wide")
    
    if st.session_state.page == "About":
        col1, col2, col3,col4,col5 = st.columns([1, 1, 1,1,1])  # Create columns to adjust centering
        with col3:
            st.image('assets/image 1.jpg', width=300, use_column_width=False)  # Adjust the width as needed        
        selected =option_menu(menu_title=None,options=["Home","About Us"],orientation="horizontal",)      
        if selected=="Home":
            st.markdown("""<h1 style='text-align: center;'>Welcome FemGuard</h1>""", unsafe_allow_html=True)
            col1, col2= st.columns([1, 1])
            with col1:
                st.header("What is FemGuard?")
                st.markdown("""
                FemGuard is an advanced hate detection model employing supervised machine learning methodologies for classifying hate speech into multiple categories. It utilizes techniques such as multi-label encoding to categorize comments into four primary labels, namely 'Misogyny,' 'Sexism,' 'Rape Threat,' and 'Body Shaming.' The model employs robust supervised machine learning algorithms such as Support Vector Machines (SVM) and Random Forest to achieve accurate classification results.
                """)
                st.header("How Does FemGuard Works?")
                st.markdown("""
              FemGuard operates through supervised machine learning, classifying text data into different categories. It begins by preprocessing the text, which involves tokenization, stop word removal, and lemmatization. Next, it extracts features using techniques like TF-IDF to convert text into numerical representations. These features are then used to train machine learning models such as Support Vector Machines (SVM) and Random Forest, enabling them to learn patterns and associations in the data.
                """)
    
                st.header("Importance of FemGuard")
                st.markdown("""
               FemGuard serves as a pivotal tool in addressing online hate speech by effectively categorizing and identifying harmful content. Its capability to classify text data into categories such as misogyny, sexism, rape threats, and body shaming makes it invaluable for monitoring and addressing abusive behavior across digital platforms.
                """)
                st.header("Get Involved")
                st.markdown("""
                We are continuously improving the FemGuard project to make it more effective and accessible. 
                If you're interested in contributing to our project or providing feedback, please check out our 
                [GitHub repository](https://github.com/knowledgefreak77/HateSpeechDetection).
                """)

                st.header("Know more About FemGuard and our Project")
                pdf_path = os.path.join("assets", "x.pdf")
                if st.button("Download PDF"):
                    with open(pdf_path, "rb") as file:
                        data = file.read()
                    st.download_button(
                        label="Click here to download the PDF",
                        data=data,
                        file_name="x.pdf",
                        mime="application/pdf"
                    )
            with col2:
                st.image('assets/image 2.jpeg', width=600, use_column_width=False)
           

            if st.button("Test FemGuard"):
                st.session_state.page = "Page 2"




        
        if selected=="About Us":
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
                st.write(f"Github Profile: [{name}]({linkedin_profile})")      
            col1, col2,col3,col4,col5 = st.columns(5)
            with col3:
                # Bolder text using HTML and CSS
                st.markdown("<p style='font-size: 34px; font-weight: bold; color: red;'>MENTOR</p>", unsafe_allow_html=True)
                # Example usage
                display_mentor("m.jpg", "Shivansh Nautiyal", "https://github.com/Shiv162003")
            col1, col2,col3,col4,col5 = st.columns(5)
            with col3:
                # Bolder text using HTML and CSS
                st.markdown("<p style='font-size: 40px; font-weight: bold; color: red;'>TEAM</p>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            # Display team members' information in each column
            with col1:
                display_team_member("3.jpg", "Kanika Thombre", "22070126052", "Kanika.Thombre.btech2022@sitpune.edu.in")
            with col2:
                display_team_member("1.jpg", "PratyushAgrawal", "22070126077", "Pratyush.Agrawal.btech2022@sitpune.edu.in")
            with col3:
                display_team_member("2.jpg", "Palak Kochey", "22070126070", "Palak.Kochey.btech2022@sitpune.edu.in")   
    elif st.session_state.page == "Page 2":
        page2()

if __name__ == "__main__":
    if "page" not in st.session_state:
        st.session_state.page = "About"
    main()
