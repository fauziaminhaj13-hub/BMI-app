import google.generativeai as genai
import streamlit as st

genai.configure(api_key="AIzaSyD2pJagmqn2MAqjtUtOtQzQdCqititU2_4")

# Initialize the model (Gemini 1.5 Turbo or Gemini Pro)
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("AI based BMI Calculator - Know your health!")

# BMI Calculator
# Take inputs from the user
name = st.text_input("Enter your name:")
wt = st.number_input("Enter your weight:")
ht = st.slider("Enter your height in cm:",50,250)
age = st.number_input("Enter your age:")
gender = st.text_input("Enter your gender:")

bmi = round(wt/(ht/100)**2,2)

st.write(f"{name}, your BMI is {bmi}")

prompt = f"Act like an expert nutritionist, comment on the BMI with the following data: height as {ht}, weight as {wt}, age as {age}, gender as {gender} and BMI as {bmi}"

# Generate content from Gemini
response = model.generate_content(prompt)

st.markdown(response.text)
