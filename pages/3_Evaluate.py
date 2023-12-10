import streamlit as st
from annotated_text import annotated_text

import dexi_bpi

st.set_page_config(layout='wide', page_title = 'Balkan Peace Index Evaluation')
st.title("BPI Evaluation")

st.markdown('This page aims at helping people evaluate Balkan Peace Index for their own values. More specifically, one can enter its own values and the results will be presented in the table below. To help with the data entry we allow selection of the existing country and its own values that can be altered.')

with st.expander('DEX Model Explanation'):
    st.markdown(
        '''
    The Balkan Peace Index is the first locally owned and locally created peace index. It was created by a team of researchers coming from the University of Belgrade (Faculty of Political Science & Faculty of Organisational Science), and it aims to introduce ‘local turn’ in a peace measurement.

    The Balkan Peace Index measures peace and peacefulness in the region of the Western Balkans. The Index consists of seven domains, with each of them having three or more indicators (for more information see Methodology). On the side of negative peace are two domains (Political Violence and Fighting Crime), while on the side of positive peace, there are five more domains (Regional and International Relations, State Capacity, Environmental Sustainability, Political Pluralism, and Socio-Economic Development).
        '''
    )
    st.image('model/bpi_graph.png')
    st.markdown('A decision- or policy-maker should enter the values for the attributes that are at the bottom of the hierarchy (does not depend on other attributes) and the inference process will start from the bottom of the hierarchy until the top of the hierarchy where the Balkan Peace Index is. The inference process is done using the decision table rules, which are developed by domain experts within this project and are evaluated externaly by focus groups and interviews.')

selected_country = st.selectbox(label='Please select a country', options=dexi_bpi.countries, index=0)

st.markdown('---')

st.subheader('Political Pluralism')

options = ['No Freedom', ' Restricted Freedom', ' Limited Freedom', ' Free']
val = dexi_bpi.get_alternative_domain(selected_country, 'Freedom of Expression and Media')
val = options.index(val)
foem = st.selectbox('Freedom of Expression and Media', options=options, index=val)
foem = options.index(foem)
foem_len = len(options)

options = ['No Freedom', ' Restricted Freedom', ' Limited Freedom', ' Free']
val = dexi_bpi.get_alternative_domain(selected_country, 'Freedom of Association')
val = options.index(val)
foa = st.selectbox('Freedom of Association', options=options, index=val)
foa = options.index(foa)
foa_len = len(options)

options = ['No Freedom', ' Restricted Freedom', ' Limited Freedom', ' Free']
val = dexi_bpi.get_alternative_domain(selected_country, 'Freedom of Assembly')
val = options.index(val)
foass = st.selectbox('Freedom of Assembly', options=options, index=val)
foass = options.index(foass)
foass_len = len(options)

options = ['Not free', ' Partly free', ' Free', ' Free and Fair']
val = dexi_bpi.get_alternative_domain(selected_country, 'Elections')
val = options.index(val)
elec = st.selectbox('Elections', options=options, index=val)
elec = options.index(elec)
elec_len = len(options)

options = ['High', ' Medium', ' Low']
val = dexi_bpi.get_alternative_domain(selected_country, 'Political Polarisation')
val = options.index(val)
pp = st.selectbox('Political Polarisation', options=options, index=val)
pp = options.index(pp)
pp_len = len(options)

st.subheader('Regional and International Relations')

options = ['Military Aggression', ' Foreign Policy and Proxies Pressure', ' Foreign Policy or Proxies Pressure', ' Public Propaganda Pressure', ' Harmonic Relations']
val = dexi_bpi.get_alternative_domain(selected_country, 'Subject to Intervention')
val = options.index(val)
soi = st.selectbox('Subject to Intervention', options=options, index=val)
soi = options.index(soi)
soi_len = len(options)

options = ['Military Aggression', ' Foreign Policy and Proxies Pressure', ' Foreign Policy or Proxies Pressure', ' Public Propaganda Pressure', ' Harmonic Relations']
val = dexi_bpi.get_alternative_domain(selected_country, 'Conducting Intervention')
val = options.index(val)
coi = st.selectbox('Conducting Intervention', options=options, index=val)
coi = options.index(coi)
coi_len = len(options)

options = ['Weak', ' Medium', ' Strong']
val = dexi_bpi.get_alternative_domain(selected_country, 'Regional Cooperation')
val = options.index(val)
ro = st.selectbox('Regional Cooperation', options=options, index=val)
ro = options.index(ro)
ro_len = len(options)

options = ['Armed', ' Non-armed', ' None']
val = dexi_bpi.get_alternative_domain(selected_country, 'Great Powers Intervention')
val = options.index(val)
gpi = st.selectbox('Great Powers Intervention', options=options, index=val)
gpi = options.index(gpi)
gpi_len = len(options)

st.subheader('State Capacity')

options = ['Low', ' Medium', ' High']
val = dexi_bpi.get_alternative_domain(selected_country, 'Support for Vulnerable Groups')
val = options.index(val)
sfvg = st.selectbox('Support for Vulnerable Groups', options=options, index=val)
sfvg = options.index(sfvg)
sffg_len = len(options)

options = ['Low', ' Medium', ' High']
val = dexi_bpi.get_alternative_domain(selected_country, 'Redistribution')
val = options.index(val)
red = st.selectbox('Redistribution', options=options, index=val)
red = options.index(red)
red_len = len(options)

options = ['Low', ' Medium', ' High']
val = dexi_bpi.get_alternative_domain(selected_country, 'Health')
val = options.index(val)
health = st.selectbox('Health', options=options, index=val)
health = options.index(health)
health_len = len(options)

options = ['Low', ' Medium', ' High']
val = dexi_bpi.get_alternative_domain(selected_country, 'Education')
val = options.index(val)
edu = st.selectbox('Education', options=options, index=val)
edu = options.index(edu)
edu_len = len(options)

options = ['Has issues', ' Does not have issues']
val = dexi_bpi.get_alternative_domain(selected_country, 'Border Demarcation')
val = options.index(val)
bordem = st.selectbox('Border Demarcation', options=options, index=val)
bordem = options.index(bordem)
bordem_len = len(options)

options = ['Low', ' Medium', ' High']
val = dexi_bpi.get_alternative_domain(selected_country, 'Sovereignty')
val = options.index(val)
sov = st.selectbox('Sovereignty', options=options, index=val)
sov = options.index(sov)
sov_len = len(options)

options = ['Yes', ' No']
val = dexi_bpi.get_alternative_domain(selected_country, 'Foreign Army and Troups')
val = options.index(val)
faat = st.selectbox('Foreign Army and Troups', options=options, index=val)
faat = options.index(faat)
faat_len = len(options)

st.subheader('Socio-economic Development')

options = ['Bad', ' Intermediate', ' Good']
val = dexi_bpi.get_alternative_domain(selected_country, 'Economic Outlook')
val = options.index(val)
ecoout = st.selectbox('Economic Outlook', options=options, index=val)
ecoout = options.index(ecoout)
ecoout_len = len(options)

options = ['Low', ' Medium', ' High']
val = dexi_bpi.get_alternative_domain(selected_country, 'Social Equity')
val = options.index(val)
socequ = st.selectbox('Social Equity', options=options, index=val)
socequ = options.index(socequ)
socequ_len = len(options)

options = ['High', ' Average', ' Low']
val = dexi_bpi.get_alternative_domain(selected_country, 'Unemployment')
val = options.index(val)
unempl = st.selectbox('Unemployment', options=options, index=val)
unempl = options.index(unempl)
unempl_len = len(options)

options = ['High', ' Average', ' Low']
val = dexi_bpi.get_alternative_domain(selected_country, 'Poverty')
val = options.index(val)
poverty = st.selectbox('Poverty', options=options, index=val)
poverty = options.index(poverty)
poverty_len = len(options)

options = ['High', ' Average', ' Low']
val = dexi_bpi.get_alternative_domain(selected_country, 'Wealth Inequality')
val = options.index(val)
wealth_in = st.selectbox('Wealth Inequality', options=options, index=val)
wealth_in = options.index(wealth_in)
wealth_in_len = len(options)

options = ['High', ' Medium', ' Low']
val = dexi_bpi.get_alternative_domain(selected_country, 'Level of Corruption')
val = options.index(val)
corr = st.selectbox('Level of Corruption', options=options, index=val)
corr = options.index(corr)
corr_len = len(options)

st.subheader('Environmental Sustainability')

options = ['Low', ' Medium', ' High']
val = dexi_bpi.get_alternative_domain(selected_country, 'Natural Resources Resilience')
val = options.index(val)
nrr = st.selectbox('Natural Resources Resilience', options=options, index=val)
nrr = options.index(nrr)
nrr_len = len(options)

options = ['Unhealthy', ' Moderate', ' Good']
val = dexi_bpi.get_alternative_domain(selected_country, 'Outdoor Air Pollution')
val = options.index(val)
oap = st.selectbox('Outdoor Air Pollution', options=options, index=val)
oap = options.index(oap)
oap_len = len(options)

options = ['High', ' Medium', ' Low']
val = dexi_bpi.get_alternative_domain(selected_country, 'Greenhouse gas emissions per capita')
val = options.index(val)
ggepc = st.selectbox('Greenhouse gas emissions per capita', options=options, index=val)
ggepc = options.index(ggepc)
ggepc_len = len(options)

options = ['Low', ' Medium', ' High']
val = dexi_bpi.get_alternative_domain(selected_country, 'Energy System Performance')
val = options.index(val)
esp = st.selectbox('Energy System Performance', options=options, index=val)
esp = options.index(esp)
esp_len = len(options)

st.subheader('Political Violence')

options = ['High Intensity', ' Medium Intensity', ' Low Intensity']
val = dexi_bpi.get_alternative_domain(selected_country, 'Conflict Intensity')
val = options.index(val)
ci = st.selectbox('Conflict Intensity', options=options, index=val)
ci = options.index(ci)
ci_len = len(options)

options = ['High Potential', ' Medium Potential', ' Low Potential']
val = dexi_bpi.get_alternative_domain(selected_country, 'Conflict Potential')
val = options.index(val)
cp = st.selectbox('Conflict Potential', options=options, index=val)
cp = options.index(cp)
cp_len = len(options)

options = ['Terror', ' Insecure', ' Full or Limited Security']
val = dexi_bpi.get_alternative_domain(selected_country, 'Political Terror')
val = options.index(val)
pt = st.selectbox('Political Terror', options=options, index=val)
pt = options.index(pt)
pt_len = len(options)

options = ['High Impact', ' Medium Impact', ' Low Impact']
val = dexi_bpi.get_alternative_domain(selected_country, 'Violent Extremism and Terrorism')
val = options.index(val)
veat = st.selectbox('Violent Extremism and Terrorism', options=options, index=val)
veat = options.index(veat)
veat_len = len(options)

st.subheader('Fighting Crime')

options = ['High', ' Medium', ' Low']
val = dexi_bpi.get_alternative_domain(selected_country, 'Violent Crime')
val = options.index(val)
vcri = st.selectbox('Violent Crime', options=options, index=val)
vcri = options.index(vcri)
vcri_len = len(options)

options = ['High', ' Medium', ' Low']
val = dexi_bpi.get_alternative_domain(selected_country, 'Organized Crime')
val = options.index(val)
org_cri = st.selectbox('Organized Crime', options=options, index=val)
org_cri = options.index(org_cri)
org_cri_len = len(options)

options = ['High', ' Medium', ' Low']
val = dexi_bpi.get_alternative_domain(selected_country, 'State Crime')
val = options.index(val)
state_cri = st.selectbox('State Crime', options=options, index=val)
state_cri = options.index(state_cri)
state_cri_len = len(options)

options = ['Poor', ' Moderate', ' Strong']
val = dexi_bpi.get_alternative_domain(selected_country, 'Human and Material Resources')
val = options.index(val)
hamr = st.selectbox('Human and Material Resources', options=options, index=val)
hamr = options.index(hamr)
hamr_len = len(options)

options = ['Poor', ' Moderate', ' Strong']
val = dexi_bpi.get_alternative_domain(selected_country, 'Judiciary Level')
val = options.index(val)
jud_l = st.selectbox('Judiciary Level', options=options, index=val)
jud_l = options.index(jud_l)
jud_l_len = len(options)

options = ['Poor', ' Moderate', ' Strong']
val = dexi_bpi.get_alternative_domain(selected_country, 'Democratic Governence')
val = options.index(val)
dem_gov = st.selectbox('Democratic Governence', options=options, index=val)
dem_gov = options.index(dem_gov)
dem_gov_len = len(options)

options = ['Not safe', ' Relatively safe', ' Safe']
val = dexi_bpi.get_alternative_domain(selected_country, 'Safety Perceptions')
val = options.index(val)
saf_perc = st.selectbox('Safety Perceptions', options=options, index=val)
saf_perc = options.index(saf_perc)
saf_perc_len = len(options)

options = ['Low', ' Medium', ' High']
val = dexi_bpi.get_alternative_domain(selected_country, 'Trust in Institutions')
val = options.index(val)
tii = st.selectbox('Trust in Institutions', options=options, index=val)
tii = options.index(tii)
tii_len = len(options)

st.markdown('---')

alt = dexi_bpi.__model.alternative("New Alternative", 
        values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                  "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                  "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                  "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                  "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                  "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                  "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                  "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                  "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                  "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                  "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

result = dexi_bpi.__model.evaluate(alt)

st.markdown('After evaluation of the alternative we see that the outcome is: ')
result = result['BPI']

_, cat_vals = dexi_bpi.get_alternatives_domain('BPI')
colors = ['#AE0017', '#A35600', 'gray', '#7B8D00', 'lightgreen']

annotated_text((f'{cat_vals[result]}', '', colors[result]))

st.markdown('---')
st.subheader('What-if Analysis')

st.markdown('One of the benefits of the analysis is the possibility to investigate if changes in a single attribute can result in better or worse Balkan Peace Index. Thus, one can find below what attributes can result in change of the outcome.')

with st.expander('Leading to worse outcome'):
    if foem > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem - 1, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Freedom of Expression and Media** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if foa > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa - 1, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Freedom of Association** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if foass > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass - 1, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Freedom of Assembly** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if elec > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec - 1, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Elections** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if pp > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp - 1, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Political Polarisation** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if soi > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi - 1, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Subject to Intervention** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if coi > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi - 1, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Conducting Intervention** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if ro > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro - 1, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Regional Cooperation** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if gpi > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi - 1, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Great Powers Intervention** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if sfvg > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg - 1, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Support for Vulnerable Groups** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if red > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red - 1, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Redistribution** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
            
    #####
    if health > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health - 1, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Health** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if edu > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu - 1, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Education** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if bordem > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem - 1, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Border Demarcation** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if sov > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov - 1, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Sovereignty** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if faat > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat - 1, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Foreign Army and Troups** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if ecoout > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout - 1, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Economic Outlook** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if socequ > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ - 1, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Social Equity** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if unempl > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl - 1, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Unemployment** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if poverty > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty - 1, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Poverty** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if wealth_in > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in - 1, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Wealth Inequality** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if corr > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr - 1, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Level of Corruption** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if nrr > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr - 1, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Natural Resources Resilience** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if oap > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap - 1, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Outdoor Air Pollution** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if ggepc > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc - 1, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Greenhouse gas emissions per capita** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if esp > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp - 1, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Energy System Performance** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if ci > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci - 1, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Conflict Intensity** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if cp > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp - 1, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Conflict Potential** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if pt > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt - 1, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Political Terror** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if veat > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat - 1, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Violent Extremism and Terrorism** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if vcri > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri - 1, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Violent Crime** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if org_cri > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri - 1, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Organized Crime** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if state_cri > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri - 1, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **State Crime** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if hamr > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr - 1, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Human and Material Resources** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if jud_l > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l - 1, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Judiciary Level** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if dem_gov > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov - 1, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Democratic Governence** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if saf_perc > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc - 1, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Safety Perceptions** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if tii > 0:
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii - 1})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        
        if result != result_alt:
            st.markdown('Depreciation in **Safety Perceptions** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

with st.expander('Leading to better outcome'):
    if foem < (foem_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem + 1, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Freedom of Expression and Media** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if foa < (foa_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa + 1, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Freedom of Association** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if foass < (foass_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass + 1, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Freedom of Assembly** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if elec < (elec_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec + 1, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Elections** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if pp < (pp_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp + 1, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Political Polarisation** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if soi < (soi_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi + 1, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Subject to Intervention** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    #####
    if coi < (coi_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi + 1, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Conducting Intervention** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    if ro < (ro_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro + 1, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Regional Cooperation** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
        
    if gpi < (gpi_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi + 1, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Great Powers Intervention** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
        
    if sfvg < (sffg_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg + 1, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Support for Vulnerable Groups** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
        
    if red < (red_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red + 1, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Redistribution** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
        
    if health < (health_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health + 1, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Health** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
        
    if edu < (edu_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu + 1, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Education** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
    
    if bordem < (bordem_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem + 1, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Border Demarcation** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
    
    if sov < (sov_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov + 1, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Sovereignty** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
    
    if faat < (faat_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat + 1, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Foreign Army and Troups** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
    
    if ecoout < (ecoout_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout + 1, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Economic Outlook** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
    
    if socequ < (socequ_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ + 1, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Social Equity** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
    
    if unempl < (unempl_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl + 1, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Unemployment** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
        
    if poverty < (poverty_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty + 1, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Poverty** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
    
    if wealth_in < (wealth_in_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in + 1, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Wealth Inequality** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
        
    if corr < (corr_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr + 1, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Level of Corruption** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
        
    if nrr < (nrr_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr + 1, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Natural Resources Resilience** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
        
    if oap < (oap_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap + 1, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Outdoor Air Pollution** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
        
    if ggepc < (ggepc_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc + 1, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Greenhouse gas emissions per capita** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
    
    if esp < (esp_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp + 1, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Energy System Performance** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
    
    if ci < (ci_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci + 1, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Conflict Intensity** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
        
    if cp < (cp_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp + 1, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Conflict Potential** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
        
    if pt < (pt_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt + 1, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Political Terror** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    if veat < (veat_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat + 1, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Violent Extremism and Terrorism** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
        
    if vcri < (vcri_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri + 1, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Violent Crime** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
        
    if org_cri < (org_cri_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri + 1, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Organized Crime** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
        
    if state_cri < (state_cri_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri + 1, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **State Crime** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
    
    if hamr < (hamr_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr + 1, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Human and Material Resources** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
        
    if jud_l < (jud_l_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l + 1, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Judiciary Level** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
        
    if dem_gov < (dem_gov_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov + 1, "Safety Perceptions": saf_perc, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Democratic Governence** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))

    if saf_perc < (saf_perc_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc + 1, "Trust in Institutions": tii})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Safety Perceptions** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))
        
    if tii < (tii_len - 1):
        alt = dexi_bpi.__model.alternative("New Alternative", 
                values = {"Freedom of Expression and Media": foem, "Freedom of Association": foa, "Freedom of Assembly": foass, 
                        "Elections": elec, "Political Polarisation": pp, "Subject to Intervention": soi, "Conducting Intervention": coi, 
                        "Regional Cooperation": ro, "Great Powers Intervention": gpi, "Support for Vulnerable Groups": sfvg, 
                        "Redistribution": red, "Health": health, "Education": edu, "Border Demarcation": bordem, 
                        "Sovereignty": sov, "Foreign Army and Troups": faat, "Economic Outlook": ecoout, "Social Equity": socequ, 
                        "Unemployment": unempl, "Poverty": poverty, "Wealth Inequality": wealth_in, "Level of Corruption": corr, 
                        "Natural Resources Resilience": nrr, "Outdoor Air Pollution": oap, "Greenhouse gas emissions per capita": ggepc, 
                        "Energy System Performance": esp, "Conflict Intensity": ci, "Conflict Potential": cp, "Political Terror": pt, 
                        "Violent Extremism and Terrorism": veat, "Violent Crime": vcri, "Organized Crime": org_cri, 
                        "State Crime": state_cri, "Human and Material Resources": hamr, "Judiciary Level": jud_l, 
                        "Democratic Governence": dem_gov, "Safety Perceptions": saf_perc, "Trust in Institutions": tii + 1})

        result_alt = dexi_bpi.__model.evaluate(alt)
        result_alt = result_alt['BPI']
        if result != result_alt:
            st.markdown('Improvement in **Safety Perceptions** will result in Balkan Peace Index being:')
            annotated_text((f'{cat_vals[result_alt]}', '', colors[result_alt]))