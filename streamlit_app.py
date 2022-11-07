import streamlit

streamlit.title('My Mom s New Healthy Diner')

streamlit.header ('Breakfast Favorites')
streamlit.text ('🍜 Omega 3 & Blueberry Oatmeal')
streamlit.text ('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text ('🐔 Hard-Boiled Free-Range Egg')
streamlit.text ('🥑🍞 Avocado toast')

streamlit.header ('🍌🍓 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruits_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruits_list = my_fruits_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruits_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruits_list.loc[fruits_selected]
#display the table on the page
streamlit.dataframe(fruits_to_show)


#New Section to display fruityvice api response
streamlit.header('fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)

# normalizando la version json
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#Mostrando la versión de json en la pantalla en forma de tabla

#conexion
import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)


add_choice = streamlit.text_input('What fruit would you like to add?','Kiwi')
streamlit.write('Thanks for adding ', add_choice)

