import streamlit as st

st.set_page_config(page_title="Mechanical Unit Converter", layout="centered")

st.title("Mechanical Unit Converter and Material Density Checker")

st.subheader("Student Information")
st.write("*Name:* Sufyan Mehmood")
st.write("*Roll Number:* 24-ME-123")

sthr = st.divider()

st.header("1. Mechanical Unit Converter")

conversion_type = st.selectbox(
    "Select Conversion Type",
    ["Length", "Mass", "Force", "Pressure"]
)

value = st.number_input("Enter Value", value=1.0)

if conversion_type == "Length":
    unit = st.selectbox("Convert From", ["meter to millimeter", "millimeter to meter", "meter to feet"])
    if unit == "meter to millimeter":
        result = value * 1000
        st.success(f"{value} m = {result} mm")
    elif unit == "millimeter to meter":
        result = value / 1000
        st.success(f"{value} mm = {result} m")
    else:
        result = value * 3.28084
        st.success(f"{value} m = {result:.3f} ft")

elif conversion_type == "Mass":
    unit = st.selectbox("Convert
