import streamlit as st
import pandas as pd
import requests


#Load Files

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

#Modify Dataframes
my_fruit_list = my_fruit_list.set_index('Fruit')

#App Code
st.title('My Parents New Healthy Diner')

st.header('Breakfast Menu')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
fruits_selected = st.multiselect('Pick some fruits:' , list(my_fruit_list.index), ['Avocado', 'Strawberries'])

if fruits_selected == []:
  fruits_selected = my_fruit_list.index

st.dataframe(my_fruit_list.loc[fruits_selected])

st.header("Fruityvice Fruit Advice!")
st.text(fruityvice_response)

# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
st.dataframe(fruityvice_normalized)
