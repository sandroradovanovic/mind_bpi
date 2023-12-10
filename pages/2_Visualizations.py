import streamlit as st
from annotated_text import annotated_text

import plotly.express as px
import plotly.graph_objects as go

import dexi_bpi 

st.set_page_config(layout='wide', page_title = 'Balkan Peace Index Visualizations')
st.title("BPI Visualizations")

st.markdown('---')

domains = ['Political Pluralism', 'State Capacity', 'Fighting Crime', 'Socio-economic Development', 'Regional and International Relations', 'Environmental Sustainability', 'Political Pluralism']
selected_domain = st.selectbox(label='Please select domain', options=domains, index=0)

with st.expander('Domain Description'):
    st.markdown(f'{dexi_bpi.get_text_domain(selected_domain)}')

st.markdown('The values presented below are ordered such that zero represents the lowest possible value, one the second lowest possible value, etc. In addition, we present the scale values colored in an approprite color -- red being the worst value and green being the best possible value. In case you would like to see the data in a tabelar form, please use the expander below')

df_vals, cat_vals = dexi_bpi.get_alternatives_domain(selected_domain)

num_vals = len(cat_vals)
columns = st.columns(num_vals)

for col in range(num_vals):
    with columns[col]:
        annotated_text((f'{col}', '', 'red' if col == 0 else 'lightgreen' if col == (num_vals - 1) else 'gray'))
        annotated_text((f'{cat_vals[col]}', '', 'red' if col == 0 else 'lightgreen' if col == (num_vals - 1) else 'gray'))

fig1 = go.Figure()

fig1.add_trace(go.Scatterpolar(
    r=df_vals['Values'].to_numpy(),
    theta=df_vals['Country'].to_numpy(),
    fill='toself',
    name=selected_domain
))
st.plotly_chart(fig1)

with st.expander('Data Table'):
    st.table(df_vals)

with st.expander('Table of Decision Rules'):
    st.table(dexi_bpi.get_decision_table(selected_domain))

st.markdown('---')
st.markdown('Here you can find valus of the subdomains and indicators for each country.')

with st.expander('Data Table'):
    st.table(dexi_bpi.get_data_table(selected_domain))