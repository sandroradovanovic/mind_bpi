import pandas as pd
import numpy as np

import dexipy.dexi as dxi

__model = dxi.read_dexi('model/BPI 2023.dxi')

def select_year(year):
    model = dxi.read_dexi(f'model/BPI {year}.dxi')

    return model

countries = [__model.alternatives[i]['name'] for i in range(len(__model.alternatives))]
attributes = [__model.attributes[i].name for i in range(len(__model.attributes))][1:]
description_text = {'Political Violence': 'Reduction of violence is a necessary, *negative* condition of peace. Political violence (direct, organised and with mass consequences), in particular, should be eliminated or reduced to consider a situation peaceful. Therefore, this domain covers various acts of political violence, such as internal and regional armed conflicts, violent crises, rebellions, violent protests, and terrorism and violent extremism acts. Regarding local knowledge, the approach of this domain primarily focuses on contextually specific patterns of violence (e.g., violence inspired by ethnoreligious rivalries and grievances, *culture of extremism* as a legacy of 1990s wars). The methodology includes relevant indices and data sets as well as document and discourse analysis (e.g., national security and defence strategies, government and NGO reports, media reports).', 
                    'Armed Conflicts and Conflict Risk': 'Armed conflict is the most destructive form of political violence, while its absence is the minimum condition for peace. Under armed conflicts, we understand “a contested incompatibility that concerns government and/or territory over which the use of armed force between the military forces of two parties, of which at least one is the government of a state, has resulted in at least 25 battle-related deaths each year” (UCDP 2014). This domain also covers the assessment of armed conflict risks or the possibility for an armed conflict to erupt. Furthermore, it includes other violent acts, such as armed rebellions, inter-communal violence, or violent incidents between the states since they can serve as a prelude to an armed conflict. The indicator measures the intensity of existing armed conflicts and the potential for future armed conflicts. It includes relevant indices and their assessments, as well as the assessment based on the analysis of political discourses in the region. It is divided into two sub-indicators: conflict intensity and conflict potential.', 
                    'Political Terror': 'The political terror domain includes all violent acts directed against “the physical integrity of the person by agents of the state” (Haschke 2021), such as torture and cruel treatment, unlawful use of deadly force, political killings, assassinations, etc. This domain covers different violent acts that are not related to armed conflicts, such as violent suppression of political demonstrations or violent repression against the political opposition. This indicator assesses the intensity of state violence against its citizen, primarily political opposition, dissidents, and similar social agents. It is mostly based on existing data sets supplemented by discourse analysis.', 
                    'Violent Extremism and Terrorism': 'Radicalisation is “change in beliefs, feelings, and behaviours in directions that increasingly justify intergroup violence and demand sacrifice in defence of intergroup” (McCauley and Moskalenko 2008). Extremism is usually understood as “the advocacy of a system of belief that claims the superiority and dominance of one identity-based ‘in-group’ over all ‘out-groups’, and propagates a dehumanizing ‘othering’ mind-set that is antithetical to pluralism and the universal application of Human Rights” (ISD 2020). For the purpose of BPI, the focus is on radicalisation and extremism that leads to violence or advocates the use of violent means. Therefore, this category includes terrorism, a closely related term, that can be defined as “the threatened or actual use of illegal force and violence by a non-state actor to attain a political, economic, religious, or social goal through fear, coercion, or intimidation” (GTD 2021). This indicator measures the intensity of this form of political violence through the mapping and counting of violent incidents and the fatalities, injuries and destruction they caused.', 
                    'Regional and International Relations': 'Peace in the six Western Balkans states and territories is often highly dependent on their mutual relations and relations with great powers. International affairs are defined as interactions among states that occur at a regional or more broad international level. These interactions could span from regional or international intervention (war, pressure, pressure through proxies) to cooperation (common foreign policy goals, participation in regional initiatives and institutions, etc.). Accordingly, the positive peace in this domain is defined as voluntarily accepted relations among the states that would create an “optimal environment for human potential to flourish” (Positive Peace Index 2020), and allow for the creation of common institutions that would nurture harmonious social relations between states and individuals. Negative peace within the international affairs domain means complete and involuntary “influence and impact of external actors in the functioning of a state” (Fragile State Index 2022). The measured impact can be political, economic, cultural, diplomatic, and military. A state or a territory can have poor, fair, good, or harmonic international relations.', 
                    'Regional Intervention': 'This indicator considers the influence and impact of regional actors on the functioning of a researched entity. As a state can both intervene in other states’ affairs and itself be an object of intervention, this indicator is divided into two sub-indicators. Sub-indicator 1 (a state or a territory is subject to intervention), and sub-indicator 2 (a state or a territory is conducting an intervention) with three possible outcomes: intervention, a non-armed intervention, or no intervention at all. Qualitative assessments of each country and territory based on key events from a year compared to the previous one. The two sub-indicators have five potential values, which span from war to positive peace, defined as harmonious relations. The values for the two sub-indicators are military aggression and occupation; foreign policy pressure (economic, political, etc., sanctions, blackmails…) AND pressure through proxies (political, economic, etc.); foreign policy pressure OR pressure through proxies; public propaganda pressure (through own media); harmonious relations.', 
                    'Regional Cooperation': 'This indicator considers the influence and impact of regional actors on the functioning of a researched entity. However, its pre-defined values differ from the I1 values, as cooperation is a qualitatively different state from intervention. Overall, the level of cooperation of a researched entity can be weak, medium, or strong. Qualitative assessments of each country and territory based on key events from a year compared to the previous one. It is assessed whether a country has weak, medium, or strong regional cooperation by applying several criteria: checking if a country is isolated or not; if there is a formal existence of regional cooperation institutions, but a country is misusing them as FP proxies; if there is a formal existence of regional cooperation institutions without the actual political consequences OR opting out of the institutions; regional cooperation institutions create policies; regional institutions benefit cooperation and serve to harmonize relations.', 
                    'Great Powers Intervention': 'As the politics, economies, culture, and diplomacy of the six Western Balkans states and territories are often highly dependent on relations with great powers, this indicator is crucial for measuring peace in the region. The indicator considers the influence and impact of great powers on the functioning of a country. As values, the sub-indicator can have armed, non-armed, or no intervention at all. The entire methodology from the regional intervention indicator applies to I3. However, since it is unlikely that the WB states could conduct interventions on great powers (USA, EU, Russia, China), I3 only considers the WB countries as being subject to great powers intervention.', 
                    'State Capacity': 'State capabilities include material resources and organizational competencies internal to the state that exist independently of political decisions about how to deploy these capabilities. State capacity represents the state’s ability to implement its goals and policies.', 
                    'Support for vulnerable groups': 'Support for vulnerable groups represents the capacity of the state to provide basic welfare for vulnerable groups and to prevent their social exclusion. The indicator assesses the capacity and outreach of state welfare programs to those groups that are recognised as marginalised in one society.', 
                    'State Provisions': 'State provisions represent the capacity of a state to provide basic services to all of its citizens and redistribute wealth inside its society.', 
                    'State Control': 'The capacity of the state to control and impose laws on its territory.', 
                    'Environmental Sustainability': 'The Index acknowledges environmental sustainability, not as a mere “stable background to the dramas emanating from sovereign states and their international relations”, but as a distinctive and active agency in the issues of survival, peace, and prosperity. Hence, environmental sustainability as a driver of “all-life support systems” preconditions both positive and negative peace. Against this backdrop, the Environmental Sustainability domain measures the relative ability of Western Balkan country to sustain its life support systems that enable/disable human and ecosystem “potential to flourish”. To gain an insight into the relative environmental sustainability of a country, this indicator focuses on the three interlinked life support systems: natural resources, air quality, and energy systems.', 
                    'Natural Resources Resilience': 'The I1 measures a countrys relative capacity (low/medium/high) to ensure the resilience of natural resources that are highly affected by climate change, such as species, water, and trees. The qualitative assessment is based on various sources encompassing international indices, state audit institutions, NGO reports, and media outlets.', 
                    'Air Quality': 'The I2 measures a countrys relative capacity (low/medium/high) to achieve recommended air quality levels and reduce the impact of air pollution on human health.', 
                    'Energy System Performance': 'The purpose of this indicator is to assess the countrys relative ability (low/medium/high) to meet current and future energy demands as well as provide environmentally responsible energy to its citizens. The qualitative assessment is based on various sources encompassing international indices, EU reports, NGO reports, and media outlets.', 
                    'Fighting Crime': 'This domain evaluates the ability of the state to combat crime threats on its territory and ensure safety for all the members of society. An efficient fight against crime is needed to prevent conflict, allow for fast post-conflict recovery, and promote stable environments in which fostering the attitudes, institutions, and structures associated with peace and development is a feasible goal.', 
                    'Crime Scale': 'This indicator evaluates the nature and level of the major crime threats in a country as they stand at the current time. The indicator is qualitative (low/medium/high) and relies on the triangulation of various sets of both qualitative and quantitative data.', 
                    'Fighting Crime Capacity': 'This indicator evaluates whether the state capacities devoted to fighting crime are sufficient and adequately used to deal with the existing levels and types of crime threats on a day-to-day basis, as well as to act as a deterrent for criminal activity in the long run. The indicator is qualitative (poor/moderate/strong) and relies on the triangulation of various sets of both qualitative and quantitative data.', 
                    'Feeling of Safety': 'This indicator evaluates whether state efforts to combat crime are found legitimate by its citizens and enhance their sense of safety. The indicator is qualitative (low/moderate/high) and relies on the triangulation of various sets of both qualitative and quantitative data.', 
                    'Political Pluralism': 'This domain assesses to what extent diverse politically articulated attitudes and interests co-exist, compete and compromise with each other, and ultimately translate into state decisions and public policies. When protected and nurtured in law and practice, pluralism in the political sphere mitigates group grievances by enabling equal participation and adequate representation in democratic processes, and free expression of criticism without fear of retribution. The domain consists of three indicators: civil liberties, elections and political polarisation. Civil liberties such as freedom of expression, association and assembly are pre-conditions for political participation. The electoral process is the key mechanism of political participation. As such, it should be based on well-defined and respected rules, on the one hand, and lead to effective and legitimate political power, on the other. Political polarisation is a corrective factor, measuring cleavages between political groups. Criteria used for assessment are predominantly qualitative. Country results in this domain can fall in four categories: bad, problematic, fairly good, and good.', 
                    'Civil Liberties': 'This indicator measures the level of respect and protection of three fundamental freedoms enabling political pluralism and participation.', 
                    'Elections': 'Elections are core democratic processes which enable reflection and transition of political pluralism into executive and legislative institutions that govern the state and social relations. It is a key mechanism through which citizens’ will ought to determine public policies. This indicator encompasses electoral conditions, conducting and monitoring elections and how election results are implemented through formation of democratic institutions and their effective use of decision-making power.', 
                    'Political Polarisation': 'Political polarisation is a negative indicator, referring to cleavages antagonizing political groups, which blocks or seriously hampers democratic institutions. It erodes social cohesion, political integration and readiness for compromise and cooperation, and it could further lead to radicalisation. It implies mutual exclusion and lack of tolerance and dialogue between opposing political camps over one or more significant issues.', 
                    'Socio-economic Development': 'Long-term peace within and between states is possible when people have fair opportunities for sustainable development. Since socio-economic development is one of the key preoccupations of governments and citizens of a society, all actors active in the process of promoting economic development in conflict-affected and conflict-prone areas should contribute to the "improvement of the economic and social conditions" in the societies in which they operate, in line with the increasingly prevalent idea of "shared value" created by Mark Kramer and Michael Porter. In this sense, this domain primarily deals with the general and context-specific characteristics of the socio-economic development of the regions economies.', 
                    'Economic Outlook': 'This indicator measures the basic components of the country’s economic performance. It consists of three pillars: basic economic performance, trade, and financial status.', 
                    'Equity': 'Equity has been one of the main values of sustainable development. It includes the provision of comparable opportunities for employment and social services.', 
                    'Levels of Corruption': 'This indicator relates to the efficiency of resource allocation. In societies with high levels of corruption, inefficient allocation of resources often leads to a reduction of funds for essential services which can further lead to dissatisfaction and civil unrest.'}


def get_alternative(name):
    idx = countries.index(name)
    return __model.alternatives[idx]

def get_alternatives_domain(domain):
    vals = [[__model.alternatives[i]['name'], __model.alternatives[i][domain]] for i in range(len(__model.alternatives))]
    df_vals = pd.DataFrame(vals, columns=['Country', 'Values'])
    df_vals = df_vals.fillna(0)
    df_vals['Values'] = df_vals['Values'].astype(int)

    att_idx = attributes.index(domain)
    cat_vals = __model.attributes[att_idx + 1].scale.scale_str().replace(' (+)', '').replace(' (-)', '').split(';')
    df_vals['Category'] = df_vals['Values'].apply(lambda x: cat_vals[x])

    return df_vals, cat_vals

def get_alternative_domain(alternative, domain):
    vals = [[__model.alternatives[i]['name'], __model.alternatives[i][domain]] for i in range(len(__model.alternatives))]
    df_vals = pd.DataFrame(vals, columns=['Country', 'Values'])
    df_vals = df_vals.fillna(0)
    df_vals['Values'] = df_vals['Values'].astype(int)

    att_idx = attributes.index(domain)
    cat_vals = __model.attributes[att_idx + 1].scale.scale_str().replace(' (+)', '').replace(' (-)', '').split(';')
    df_vals['Category'] = df_vals['Values'].apply(lambda x: cat_vals[x])

    return df_vals['Category'].loc[df_vals['Country'] == alternative].values[0]

def get_text_domain(domain):
    return description_text[domain]

def get_decision_table(domain):
    dom_idx = attributes.index(domain) + 1

    att_idx = np.where([__model.attributes[i].parent.name == domain for i in range(len(__model.attributes))])[0].tolist()
    atts_child = [__model.attributes[i].name for i in att_idx]
    atts = str(__model.attributes[dom_idx].funct.values.keys()).replace(' ', '').replace('(', '').replace(')', '').replace('dict_keys[', '').replace(']', '').split(',')
    atts = np.array(atts).reshape((int(len(atts)/len(atts_child)), len(atts_child))).astype('int')

    atts_values = []
    for j in range(len(atts_child)):
        to_append = [__model.attributes[att_idx[j]].scale.values[i] for i in atts[:, j]]
        atts_values.append(to_append)
    
    label = np.array(str(__model.attributes[dom_idx].funct.values.values()).replace('dict_values([', '').replace('])', '').replace(' ', '').split(',')).astype(int)
    label = [__model.attributes[dom_idx].scale.values[i] for i in label]

    df_rules = pd.DataFrame(np.array(atts_values).T.tolist(), columns=atts_child)
    df_rules[domain] = label

    return df_rules

def __get_children(domain):
    att_idx = np.where([__model.attributes[i].parent.name == domain for i in range(len(__model.attributes))])[0].tolist()
    atts_child = [__model.attributes[i].name for i in att_idx]

    return atts_child, att_idx

def __get_children_for_domain(domain):
    atts_child = []

    children, _ = __get_children(domain)

    if len(children) > 0:
        atts_child.append(children)
        for child in children:
            atts_child.append(__get_children_for_domain(child))

    return atts_child

def __flatten(lst):
    return [item for sublist in lst for item in (__flatten(sublist) if isinstance(sublist, list) else [sublist])]

def get_data_table(domain):
    atts = __flatten(__get_children_for_domain(domain))
    df_data = []

    for att in atts:
        att_idx = attributes.index(att) + 1
        for country in __model.alternatives:
            cat_vals = __model.attributes[att_idx].scale.scale_str().replace(' (+)', '').replace(' (-)', '').split(';')
            if country[att] is None:
                df_data.append([country['name'], att, ""])
            elif isinstance(country[att], set):
                df_data.append([country['name'], att, list(country[att])[0]])
            else:
                df_data.append([country['name'], att, cat_vals[country[att]]])

    df_data = pd.DataFrame(df_data, columns=['Country', 'Attribute', 'Value'])
    df_data = df_data.pivot(index='Country', columns='Attribute', values='Value')

    return df_data

def return_aggregate_attributes(attributes):
    atts = []
    for i in range(len(__model.attributes)):
        for a in attributes:
            if __model.attributes[i].name == a:
                if __model.attributes[i].is_aggregate():
                    atts.append(__model.attributes[i].name)
    
    return atts

# __model.attributes[1].scale.scale_str()