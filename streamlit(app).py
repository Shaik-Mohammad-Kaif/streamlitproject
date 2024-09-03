import streamlit as st
st.markdown(
    """
    <style>
    /* Sidebar background color */
    [data-testid="stSidebar"] {
        background-color: #075d7a;
         color : white;
         box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
    }
    /* Sidebar text color for headers, text input, etc. */
    [data-testid="stSidebar"] * {
        color: white;  /* Set the text color to white */
    }
   [data-testid="stSidebar"] .stTextInput, 
    [data-testid="stSidebar"] .stButton, 
    [data-testid="stSidebar"] .stSelectbox {
        color: black;  /* Optionally, set input text color to black */
          /* Optional: dark background for inputs */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Welcome To :red[Kaif TechBuddy]")
st.header("Google Generative AI Certification")
#st.info("2024 google introduction to generative AI certification program")
#st.warning("Fill all the details carefully")
#st.error("Try again")
st.text_input("Enter Name")
st.text_input("Enter Password")
st.date_input("Enter DOB")
st.radio("Select Gender",["Male","Female","Others"])
st.multiselect("Choose Skills",["Data SCience","AI","Frontend","Backend","Machine Learning"])
st.file_uploader("Upload Photo")
st.button(":blue[Submit]")
st.sidebar.markdown("# Kaif TechBuddy")
st.sidebar.text_input("Enter Username")
st.sidebar.text_input("Enter Your Password")
st.sidebar.button(":blue[Click]")
