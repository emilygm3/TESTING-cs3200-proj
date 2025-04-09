import streamlit as st

# Add a title to the app
st.title("My Streamlit App")

# Add a slider
value = st.slider("Select a value", 0, 100, 50)

# Display the value
st.write("You selected:", value)