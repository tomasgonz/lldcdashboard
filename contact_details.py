import json
import pandas as pd

# Load the JSON data
with open('./data.json', encoding='utf-8') as file:
    data = json.load(file)

# List of Landlocked Developing Countries (LLDCs)
lldcs_list = [
    "Afghanistan", "Armenia", "Azerbaijan", "Bhutan", "Bolivia (Plurinational State of)", "Botswana", 
    "Burkina Faso", "Burundi", "Central African Republic", "Chad", "Ethiopia", 
    "Kazakhstan", "Kyrgyzstan", "Lao People's Democratic Republic", "Lesotho", 
    "Malawi", "Mali", "Moldova", "Mongolia", "Nepal", "Niger", "North Macedonia", 
    "Paraguay", "Rwanda", "South Sudan", "Eswatini", "Tajikistan", "Turkmenistan", 
    "Uganda", "Uzbekistan", "Zambia", "Zimbabwe"
]

# Filter the data for LLDCs and extract country and email
lldcs_data = []
for country in data['countries']:
    # Check if any word from lldcs_list is contained in country['MC_EntityLong']
    if any(lldc in country['MC_EntityLong'] for lldc in lldcs_list):
        country_name = country['MC_EntityLong']
        email = country['MC_eMail']
        lldcs_data.append({'country': country_name, 'email': email})

# Convert to DataFrame
lldcs_df = pd.DataFrame(lldcs_data)

# Saving to Excel
excel_path = 'LLDCs_emails.xlsx'
lldcs_df.to_excel(excel_path, index=False)

excel_path
