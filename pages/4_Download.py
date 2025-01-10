import pandas as pd

import streamlit as st
from annotated_text import annotated_text

import dexi_bpi

import base64

st.set_page_config(layout='wide', page_title = 'Balkan Peace Index Downloads')
st.title("BPI Download Section")

st.markdown('This page aims to open the model and results to the broader audience for inspection and further research. Please find below the datasets and the DEX project.')

year = st.selectbox('Please select year:', options=[2022, 2023, 2024], index=2)
dexi_bpi.__model = dexi_bpi.select_year(year)

@st.cache_resource
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

df, _ = dexi_bpi.get_alternatives_domain('BPI')
csv = convert_df(df)

st.download_button(
    label="Download Final Results",
    data=csv,
    file_name='final_result.csv',
    mime='text/csv',
)


df_all = dexi_bpi.get_data_table('root')
csv = convert_df(df_all)

st.download_button(
    label="Download the Entire Data",
    data=csv,
    file_name='all_data.csv',
    mime='text/csv',
)

st.markdown('---')
st.markdown('In case you would like to download a table of decision rules, please select an attribute from the dropdown menu, and press the download button.')

domains = ['BPI', 'Positive Peace Domains', 'Negative Peace Domains', 'Political Pluralism', 'State Capacity', 'Fighting Crime', 'Socio-economic Development', 'Regional and International Relations', 'Environmental Sustainability', 'Political Pluralism']
selected_domain = st.selectbox(label='Please select domain', options=domains, index=3)

df_rules = dexi_bpi.get_decision_table(selected_domain)
csv = convert_df(df_rules)

st.download_button(
    label="Download the Decision Rules",
    data=csv,
    file_name=f'{selected_domain}_decision_rules.csv',
    mime='text/csv',
)

st.markdown('In case you would like to go deeper in the DEX model and get rules for the subdomains and indicators, please use the dropdown menu below.')
atts = dexi_bpi.__flatten(dexi_bpi.__get_children_for_domain(selected_domain))
atts = dexi_bpi.return_aggregate_attributes(atts)
selected_att = st.selectbox(label='Please select attribute', options=atts, index=0)

df_rules = dexi_bpi.get_decision_table(selected_att)
csv = convert_df(df_rules)

st.download_button(
    label=f"Download the Decision Rules for {selected_att}",
    data=csv,
    file_name=f'{selected_att}_decision_rules.csv',
    mime='text/csv',
)

st.markdown('---')
st.markdown(
    '''
    If you want to try out the DEX software, we invite you to download the [DEXi: A Program for Multi-Attribute Decision Making](https://kt.ijs.si/MarkoBohanec/dexi.html) and load the project yourselves.
    '''
)

def get_file_content_as_base64(file_path):
    with open(file_path, "rb") as file:
        data = file.read()
    return data

file_path = f"model/BPI {year}.dxi"

st.download_button(
    label="Download the DEXi file",
    data=get_file_content_as_base64(file_path),
    file_name='Balkan Peace Index.dxi',
    mime='application/octet-stream',
)