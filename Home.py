import json

import streamlit as st
from annotated_text import annotated_text

import plotly.express as px

import dexi_bpi

st.set_page_config(layout='wide', page_title = 'Balkan Peace Index')

st.title("Balkan Peace Index")

# DESCRIPTION
st.markdown('Balkan Peace Index is a part of the [MIND](https://mindproject.ac.rs/) project. MIND project aims to bust the myths about the Western Balkans as a perpetual "powder keg" and to provide local and contextual knowledge about security cooperation and peace dynamics in the region.')
st.markdown('Please use this page to inspect the methodology and outcomes of the Balkan Peace Index, as well as to see visualizations of data, download the data, and evalute a hypothetical country and policy-making implications.')

# EXPANDER
with st.expander('The state of peace in Balkans'):
    st.markdown('From a global perspective, the Western Balkans is regarded as a highly peaceful region. It has been free of armed conflicts for more than twenty years. Although still burdened by the 1990s war legacy and political and ethnic conflicts, it displays low levels of political violence. In 2022 only Kosovo* was affected by the violent crisis, while all other conflicts in the region, including the highly polarised one in Bosnia and Herzegovina (BiH), are estimated as political disputes or non-violent crises. Therefore, on the Balkan Peace Index (BPI) scale, Kosovo and Bosnia are ranked as contested peace, Serbia and Montenegro as polarised peace, North Macedonia as stable peace, and Albania and Croatia as consolidated peace.')
    st.markdown('Kosovo and Bosnia remain neuralgic issues of the region. Both are cases of permanent political crisis since the sovereignty of the former is contested from the outside, while the sovereignty of the latter is disputed from the inside. Clashes between the Albanian majority and Serbian minority in Kosovo, the Serbian and Kosovo government, or between Republika Srpska and the central government in BiH, and Croatian and Bosniak representatives in the Federation of BiH, are the main causes of instability in the region. Although long-lasting crises, these two cases have little potential to escalate into limited or full wars. The main reason for that is the presence of international peacekeeping forces that can contain the possible spread of violence. However, these conflicts can spark occasional violent incidents.')
    st.markdown('BPI estimates regional cooperation as satisfying, although most regional actors conducted interventions through proxies and foreign policy pressures. Again, the disputed status of Kosovo, and the interference of Croatia and Serbia in the internal issues of Bosnia and Herzegovina, have limited the potential of cooperation in the region. A profound political crisis in Montenegro has also caused many turbulences in the region. On the positive side, there were some successful regional initiatives regarding the status of the Orthodox Church in Montenegro and Macedonia, or the "Open Balkan" community.')
    st.markdown('Another challenge for the peace in the region is state capacity. In particular, Kosovo, Bosnia and Herzegovina, and Albania are estimated as having a low capacity for supporting vulnerable groups, state provisions in education, health and redistribution, or control of territory. Bosnia and Kosovo are specific cases since they host foreign troops on their territory and cannot control it effectively. Serbia is another case of low state control capacity, for it considers Kosovo its integral part and cannot exercise sovereignty over it.')
    st.markdown('The Western Balkan region is one of the most severely affected by climate change in Europe. Notwithstanding Croatia and Albania, all other countries and territories have performed poorly in terms of environmental sustainability. The air quality seems to be at an all-time low, and citizens of the Western Balkans are being exposed to severely unhealthy air pollution quite more than inhabitants of other parts of Europe. The current tensions surrounding the war in Ukraine, which led to a substantial increase in the prices of electricity and derivatives, also affected the performance of the energy systems in the region.')
    st.markdown('Fighting crime in the Western Balkans remains a severe impediment to regional peace, security, and development. The overall capacities, efforts and results in fighting crime have been estimated as poor in four out of seven countries/territories in the region for the reported period, with the rest three having only moderate success. While Croatia does stand out in progress made, the entire region remains susceptible to all kinds of crimes, from conventional, via organised to state crime. Post-conflict legacy, political instability, inter-ethnic tensions, and, above all, poverty and lack of employment opportunities keep the region in a vicious circle in which criminality does not allow any significant progress in the consolidation of the peace and development on the local, national, and regional level.')
    st.markdown('Political pluralism in the region is restricted. Freedoms of expression, association, and assembly are mostly limited. Elections are partly free or free but generally unfair, with medium or high levels of political polarisation. The only exception is Croatia, which has a high level of protection for freedom of expression and media, association and assembly, free and fair elections, and a low level of polarisation.')
    st.markdown('The level of socio-economic development of the region is rated as medium. This represents the expected result considering the average values of socio-economic development for four regional actors (Albania, Montenegro, North Macedonia, and Serbia), two poor results (Bosnia and Herzegovina and Kosovo), and only one high outcome (Croatia)')
    st.markdown('Out of seven BPI domains, the Western Balkan Region performed excellently in only one – political violence. At the same time, it gained poor scores in domains of environmental sustainability and fighting crime and average scores in regional and international relations, state capacity, political pluralism, and socio-economic development. That is to say that the region can be considered highly peaceful in terms of negative peace or the absence of direct (armed) violence. Nonetheless, the level of positive peace (the absence of structural violence) remains between poor and average, although with an upward trend.')

year = st.selectbox('Please select year:', options=[2022, 2023], index=1)
dexi_bpi.__model = dexi_bpi.select_year(year)

# MAP
df, cat_vals = dexi_bpi.get_alternatives_domain('BPI')
df['Color'] = df['Values'].map({1: '#AE0017', 2: '#A35600', 3: 'gray', 4: '#7B8D00', 5: 'lightgreen'})
color_map = {1: '#AE0017', 2: '#A35600', 3: 'gray', 4: '#7B8D00', 5: 'lightgreen'}

num_vals = len(cat_vals)
columns = st.columns(num_vals)
colors = ['#AE0017', '#A35600', 'gray', '#7B8D00', 'lightgreen']

for col in range(num_vals):
    with columns[col]:
        annotated_text((f'{col}', '', colors[col]))
        annotated_text((f'{cat_vals[col]}', '', colors[col]))
st.table(df.drop(['Values', 'Color'], axis=1))

with open('model/custom.geo.json', 'r', encoding='utf-8') as file:
    geojson_data = json.load(file)

fig = px.choropleth(df,
                    geojson=geojson_data,
                    locations='Country',
                    featureidkey="properties.name",
                    color='Values',
                    color_discrete_map=color_map,
                    hover_name='Country',
                    title='Map of Balkan Peace Index')

fig.update_geos(center=dict(lon=20, lat=44),
                projection_scale=20)

st.plotly_chart(fig)