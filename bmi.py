import streamlit as st

# Apply CSS styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f0f5;
    }
    h1 {
        color: #333333;
        text-align: center;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    .stTextInput>div>input {
        border: 2px solid #4CAF50;
        padding: 10px;
        border-radius: 5px;
    }
    .stRadio>div>div>label {
        font-size: 18px;
    }
    .stNumberInput>div>input {
        border: 2px solid #4CAF50;
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# App title
st.title("BMI Calculator")
bmi=0
height=0

# Input weight
weight = st.number_input("Enter weight in kg")

# Input height format
status = st.radio("Select your height format:", ('cm', 'm', 'feet'))

# Input height based on selected format
if status == 'cm':
    height = st.number_input(' enter height in Centimeters')
    try:
        bmi = weight / ((height / 100) ** 2)
    except:
        st.text("Enter some height values")
elif status == 'm':
    height = st.number_input("Enter height in meters")
    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter some height values")
elif status == 'feet':
    height = st.number_input('enter height in Feet')
    try:
        bmi = weight / ((height / 3.28) ** 2)
    except:
        st.text("Enter some height values")

# Calculate BMI button
if st.button("Calculate bmi"):
    st.text("Your BMI index is {:.2f}".format(bmi))
    if bmi < 16:
        st.error("You are Extremely Underweight")
    elif 16 <= bmi < 18.5:
        st.warning("You are Underweight")
    elif 18.5 <= bmi < 25:
        st.success("Healthy")
    elif 25 <= bmi < 30:
        st.warning("Overweight")
    elif bmi >= 30:
        st.error("Extremely Overweight")
