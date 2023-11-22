import streamlit as st
from databricks import sql


st.title('Hello Ben')
st.header('Testing Streamlit')
st.text("This is my first data app on Streamlit!")
st.text_input('Fist name')
st.number_input('Pick a number',0,10)

with sql.connect(server_hostname = 'adb-2220921394648299.19.azuredatabricks.net',
                 http_path       = '/sql/1.0/warehouses/56f5c8dc87549f71',
                 access_token    = 'dapi5f44d54248affbb1bc521851ad026e08') as connection:

  with connection.cursor() as cursor:
    cursor.execute("SELECT * from cdr_raw.airport_location limit 2")
    result = cursor.fetchall()

    print('1')
    for row in result:
      print(row)
      st.text(row)
