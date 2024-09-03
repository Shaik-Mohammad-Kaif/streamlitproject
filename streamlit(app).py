import streamlit as st
from PIL import Image

# Custom CSS for sidebar and buttons
st.markdown(
    """
    <style>
    /* Sidebar background color */
    [data-testid="stSidebar"] {
        background-color: #2c3e50;
        color: white;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
    }
    /* Sidebar text color for headers, text input, etc. */
    [data-testid="stSidebar"] * {
        color: white;  /* Set the text color to white */
    }
    [data-testid="stSidebar"] .stTextInput,
    [data-testid="stSidebar"] .stButton,
    [data-testid="stSidebar"] .stSelectbox {
        color: blue;  /* Set input text color to blue */
    }
    /* Main content background color */
    .main-content {
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    }
    /* Header text color */
    .header-text {
        color: #2c3e50;
        font-weight: bold;
    }
    /* Button styles */
    .stButton button {
        background-color: #4CAF50; /* Green background */
        color: white; /* White text */
        padding: 10px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #45a049; /* Darker green for hover effect */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown("<h1 class='header-text'>Welcome to Kaif TechBuddy</h1>", unsafe_allow_html=True)

# Main content
with st.container():
    st.markdown("<h2 class='header-text'>Google Generative AI Certification</h2>", unsafe_allow_html=True)
    st.write("Please fill out the form below")

    # Create columns for better layout
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Enter Name")
        password = st.text_input("Enter Password", type="password")
        dob = st.date_input("Enter DOB")
        gender = st.radio("Select Gender", ["Male", "Female", "Others"])

    with col2:
        skills = st.multiselect("Choose Skills", ["Data Science", "AI", "Frontend", "Backend", "Machine Learning"])
        photo = st.file_uploader("Upload Photo")

    # Submit button
    if st.button("Submit"):
        st.success(f"Thank you, {name}!")

        # Display entered details
        st.subheader("Your Entered Details:")
        st.write(f"**Name:** {name}")
        st.write(f"**Date of Birth:** {dob}")
        st.write(f"**Gender:** {gender}")
        st.write(f"**Skills:** {', '.join(skills)}")

        if photo:
            img = Image.open(photo)
            st.image(img, caption="Uploaded Photo", use_column_width=True)

# Sidebar content
with st.sidebar:
    st.markdown("# Kaif TechBuddy")
    st.text_input("Enter Username")
    st.text_input("Enter Your Password", type="password")
    st.button("Click")
