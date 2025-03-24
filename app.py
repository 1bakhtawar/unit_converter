import streamlit as st
## Function

def distance_converter(from_unit,to_unit,value):
    units = {
        "meter" : 1,
        "kilometer" : 1000,
        "feet" : 0.3048,
        "miles": 1609.34
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def temperature_converter(from_unit, to_unit, value):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        result = (value * 9/5) + 32
    elif from_unit == "Fahrenteit" and to_unit == "Celsius":
        result = (value - 32) * 5/9
    else:
        result = value
    return result

def weight_converter (from_unit,to_unit,value):
    units = {
        "Kilograms" : 1,
        "Grams" : 0.001,
        "Pounds" : 0.453592,
        "Ounces": 0.0283495
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def pressure_converter (from_unit,to_unit,value):
    units = {
        "Pascal" : 1,
        "Hectopascals" : 100,
        "Kilopascals" : 1000,
        "Bar": 100000
    }
    result = value * units[from_unit] / units[to_unit]
    return result


# UI
st.title("🎉 Welcome to Unit Converter")

st.write("Select a value and get the converter value")

#Select Category
category = st.selectbox("Choose a Category" , ["Distance" , "Temperature" ,"Weight" , "Pressure"])

if category == "Distance":
    from_unit = st.selectbox("From",["meter" , "kilometer" , "feet" , "miles"])
    to_unit = st.selectbox("To",["meter" , "kilometer" , "feet" , "miles"])
    value = st.number_input("Enter a value")
    if st.button("Convert"):
        result = distance_converter(from_unit, to_unit,value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Temperature":
    from_unit = st.selectbox("From",["Celsius" , "Fahrenheit"])
    to_unit = st.selectbox("To",["Celsius" , "Fahrenheit"])
    value = st.number_input("Enter a value")
    if st.button("Convert"):
        result = temperature_converter(from_unit, to_unit,value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")


elif category == "Weight":
    from_unit = st.selectbox("From",["Kilograms" , "Grams" , "Pounds" , "Ounces"])
    to_unit = st.selectbox("To",["Kilograms" , "Grams" , "Pounds" , "Ounces"])
    value = st.number_input("Enter a value")
    if st.button("Convert"):
        result = weight_converter(from_unit, to_unit,value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")


elif category == "Pressure":
    from_unit = st.selectbox("From",["Pascal" , "Hectopascals" , "Kilopascals" , "Bar"])
    to_unit = st.selectbox("To",["Pascal" , "Hectopascals" , "Kilopascals" , "Bar"])
    value = st.number_input("Enter a value")
    if st.button("Convert"):
        result = pressure_converter(from_unit, to_unit,value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")