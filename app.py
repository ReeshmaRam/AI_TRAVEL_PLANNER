import streamlit as st
from src.core.planner import TravelPlanner
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e");
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="AI travel planner")
st.title("AI Travel Itinerary Planner ")
st.write("plan your day trip itinerary by entering  your city and interests")
import os
from dotenv import load_dotenv
load_dotenv()
with st.form("🌍 planner form"):
    city=st.text_input("Enter the city you are visiting")
    interests=st.text_input("Enter your interests (comma separated)")
    submitted=st.form_submit_button("Create Itinerary")
    if submitted:
        if city and interests:
            planner=TravelPlanner()
            planner.set_city(city)
            planner.set_interests(interests)
            itineary=planner.create_itineary()
            st.subheader("Your Itinerary ")
            st.markdown(itineary)
        else:
            st.warning("Please enter both city and interests to move forward")    