import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Flight Price Predictor", layout="centered")
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #e0f7fa, #ffffff);
        color: #000000;
    }
    h1, h2, p {
        color: #4B0082;
    }
    .stButton>button {
        background-color: #CC95FF;
        color: #ffffff;
        font-weight: bold;
        border-radius: 12px;
        height: 45px;
        width: 220px;
        font-size: 16px;
        transition: background 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #6a0dad;
    }
    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    input[type="number"] {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)



model = pickle.load(open("model.pickle", "rb"))

st.markdown("<h1 style='text-align: center;'>✈️ Flight Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #333333;'>Enter flight details below to get estimated price</p>", unsafe_allow_html=True)
st.markdown("---")

airline_options = {'AirAsia':0, 'Indigo':1, 'GO_FIRST':2, 'SpiceJet':3, 'Air India':4, 'Vistara':5}
source_city_options = {'Delhi':0, 'Hyderabad':1, 'Bangalore':2, 'Mumbai':3, 'Kolkata':4, 'Chennai':5}
destination_city_options = {'Delhi':0, 'Hyderabad':1, 'Mumbai':2, 'Bangalore':3, 'Chennai':4, 'Kolkata':5}
departure_time_options = {'Early Morning':0, 'Morning':1, 'Afternoon':2, 'Evening':3, 'Night':4, 'Late Night':5}
arrival_time_options = {'Early Morning':0, 'Morning':1, 'Afternoon':2, 'Evening':3, 'Night':4, 'Late Night':5}
stops_options = {'Zero':0, 'One':1, 'Two or More':2}
class_options = {'Economy':0, 'Business':1}

col1, col2 = st.columns(2)

with col1:
    airline = st.selectbox("Airline", list(airline_options.keys()), key="airline_select")
    source_city = st.selectbox("Source City", list(source_city_options.keys()), key="source_select")
    departure_time = st.selectbox("Departure Time", list(departure_time_options.keys()), key="dep_time")
    stops = st.selectbox("Stops", list(stops_options.keys()), key="stops_select")

with col2:
    destination_city = st.selectbox("Destination City", list(destination_city_options.keys()), key="dest_select")
    arrival_time = st.selectbox("Arrival Time", list(arrival_time_options.keys()), key="arr_time")
    flight_class = st.selectbox("Class", list(class_options.keys()), key="class_select")
    extra_feature = st.number_input("Additional Feature (numeric)", min_value=0, value=1, key="extra_feature")

st.markdown("---")

if st.button("Predict Price", key="predict_btn"):
    input_data = np.array([[
        airline_options[airline],
        source_city_options[source_city],
        destination_city_options[destination_city],
        departure_time_options[departure_time],
        arrival_time_options[arrival_time],
        stops_options[stops],
        class_options[flight_class],
        extra_feature
    ]])
    
    prediction = model.predict(input_data)
    st.success(f"💰 Estimated Flight Price: ₹{round(prediction[0],2)}")
    st.balloons()







