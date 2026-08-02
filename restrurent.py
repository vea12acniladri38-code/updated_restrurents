import streamlit as st
from google import genai

# Gemini API
api_key = st.secrets["GOOGLE_API_KEY"]

client = genai.Client(api_key=api_key)

st.set_page_config(
    page_title="🍽️ AI Restaurant Finder",
    page_icon="🍽️"
)

st.title("🍽️ AI Restaurant Finder")

st.write("Find restaurant recommendations based on your preferences.")

city = st.text_input("📍 Enter your city")

cuisine = st.selectbox(
    "🍕 Preferred Cuisine",
    [
        "Any",
        "Indian",
        "Chinese",
        "Italian",
        "Mexican",
        "Thai",
        "Japanese",
        "American",
        "South Indian",
        "North Indian",
        "Street Food"
    ]
)

budget = st.selectbox(
    "💰 Budget",
    [
        "Under ₹500",
        "₹500 - ₹1000",
        "₹1000 - ₹2000",
        "Above ₹2000"
    ]
)

food_type = st.radio(
    "🥗 Food Preference",
    [
        "Vegetarian",
        "Non-Vegetarian",
        "Both"
    ]
)

occasion = st.selectbox(
    "🎉 Occasion",
    [
        "Casual Lunch",
        "Dinner",
        "Birthday",
        "Date",
        "Family Outing",
        "Friends Hangout"
    ]
)

if st.button("🍽️ Find Restaurants"):

    if city == "":
        st.warning("Please enter your city.")
        st.stop()

    prompt = f"""
You are a restaurant expert.

Recommend five restaurants.

City:
{city}

Cuisine:
{cuisine}

Budget:
{budget}

Food Preference:
{food_type}

Occasion:
{occasion}

For each restaurant provide:

Restaurant Name

Cuisine

Approximate Cost

Why it is recommended

Must Try Dish

Keep the response under 300 words.

If you are unsure of exact restaurant names for the city, say they are suggestions and encourage the user to verify current details before visiting.
"""

    with st.spinner("Finding restaurants..."):

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

    st.subheader("🍽️ Restaurant Recommendations")

    st.write(response.text)

st.markdown("---")

st.caption(
    "Recommendations are AI-generated and may not reflect current menus, prices, or availability. Please verify details before visiting."
)
