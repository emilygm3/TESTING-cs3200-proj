import logging
logger = logging.getLogger(__name__)
import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import world_bank_data as wb
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from modules.nav import SideBarLinks

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header('World Bank Data')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['first_name']}.")

# get the countries from the world bank data
with st.echo(code_location='above'):
    countries:pd.DataFrame = wb.get_countries()
   
#    st.dataframe(countries)

# the with statment shows the code for this block above it 
with st.echo(code_location='above'):
    arr = np.random.normal(1, 1, size=100)
    test_plot, ax = plt.subplots()
    ax.hist(arr, bins=20)

    st.pyplot(test_plot)


with st.echo(code_location='above'):
    slim_countries = countries[countries['incomeLevel'] != 'Aggregates']
    data_crosstab = pd.crosstab(slim_countries['region'], 
                                slim_countries['incomeLevel'],  
                                margins = False) 
    st.table(data_crosstab)

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")


col1, col2, col3 = st.columns(3)

# Add select box to the first column
with col1:
    text_input = st.text_input(
    "Search Flights",
    key="placeholder")
    st.write(text_input)
    date = st.selectbox("Dates", ["3/4", "3/5", "3/6"])
    airline = st.selectbox("Airline", ["United", "Spirit", "RyanAir"])
    price = st.selectbox("Price", ["$450", "$250", "$20"])
    num_stops = st.selectbox("Stops", ["0", "1", "2"])
    duration = st.selectbox("Total Duration", ["180", "450", "320"])

# Add select box to the second column
with col2:
    option1 = st.selectbox("From", ["BOS", "LHR", "LTN"])

with col3:
    option2 = st.selectbox("To", ["BOS", "LHR", "LTN"])



    
