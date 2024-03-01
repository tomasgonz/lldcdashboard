import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# This is to read a csv file into a pandas object
# Here we have created an object called data_on_electricity
doe = pd.read_csv('API_EG.ELC.ACCS.ZS_DS2.csv')

# Crate an option on the sidebar to allow for the selection of a sepecific country
selected_country = st.sidebar.selectbox('Select a country, jajaja', doe['Country Name'])

# Using the selected country name, filters the data only for that country
selected_country_data = doe[doe['Country Name'] == selected_country]

st.write(selected_country_data)

# Transform the data from wide format into long format
df_long = pd.melt(selected_country_data, id_vars=['Country Name'], var_name='Year', value_name='Value')

st.write(df_long)

plt.figure(figsize=(10, 6))
# Create the plot
fig, ax = plt.subplots()
ax.plot(df_long['Year'], df_long['Value'], marker='x')
ax.set_title('Percentage of population with access to electricity')
ax.set_xlabel('Year')
ax.set_ylabel('%')

# Display the plot in Streamlit
st.pyplot(fig)

# This is to calculate the mean of a series
st.write(doe['2020'].mean())

# This allows us to select the top 10 rows
df_10 = doe[:10]

# Another crazu object

df_10_2020 = df_10[['Country Name', '2020']]

# This code allows to extract two columns
st.write(df_10[['Country Name','2019', '2020']])

# This code allows to extract two columns
st.write(df_10[['Country Name', '2019', '2020']])

# Create the plot
fig, ax = plt.subplots()
ax.bar(df_10['Country Name'], df_10['2020'])

ax.set_title('Plot Title')
ax.set_xlabel('Column1')
ax.set_ylabel('Column2')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")  # Rotate labels by 45 degrees and align right
# Display the plot in Streamlit
st.pyplot(fig)