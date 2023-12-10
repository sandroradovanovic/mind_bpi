import streamlit as st
from annotated_text import annotated_text

st.set_page_config(layout='wide', page_title = 'Balkan Peace Index Methodology')
st.title("BPI Methodology")

st.markdown(
    '''
    The Balkan Peace Index employs the DEX (DEcision eXpert) method for the evaluation of its domains, indicators, and sub-indicators. DEX is a qualitative, hierarchical, and rule-based multi-criteria decision-making (MCDM) method (Bohanec, 2022). MCDM provides a general approach and a multitude of methods that allow the decision maker to formulate their objectives in terms of multiple, possibly conflicting, criteria, and represent them in the form of a multi-criteria model. The model is subsequently used to evaluate and analyse decision alternatives, with the aim to help the decision maker to understand the decision situation and properties of individual alternatives, to rank them and/or choose the best one, and to justify the decision.


    DEX has the following characteristics (Trdin & Bohanec, 2018): It is *qualitative*: decision criteria are represented by variables, called attributes, which can take only discrete values. Those are usually words rather than numbers, for instance “bad”, “medium”, “excellent”, “low”, or “high”. It is *hierarchical*: a DEX model consists of hierarchically structured attributes; the structure represents the decomposition of a decision problem into smaller and potentially more manageable sub-problems. It is *rule-based*: the evaluation of alternatives is defined with decision rules, acquired, and represented in the form of decision tables.
    '''
)

st.image('model/algo-based-indexing.png')
st.markdown('Figure 1. General concept of DEX models.')

st.markdown(
    '''
    Formally, a DEX model (Figure 1) consists of attributes X = {x1,x2,…,xn,x1',x2', …,xm', y} . Generally, an attribute is a variable that represents some observed property of alternatives. The notation reflects the position and role of individual attributes in the model hierarchy:
    
    - x1,x2,…,xn are called basic attributes and serve as inputs to the model.
    - x1',x2', …,xm' are aggregate attributes. Each of them serves both as an output of some sub-tree and input to the level above.
    - y is also an aggregate attribute, however it is the most important one. It represents the main output of the model: evaluation of decision alternatives.
    
    Each attribute x1,x2,…,xn,x1',x2', …,xm', y can take values from corresponding value scales, denoted X1,X2,…,Xn,X1',X2', …,Xm', Y, respectively. Value scales are discrete and are typically represented by words, for instance X1={"low", "medium", "high"}. The number of possible values in a single scale is generally small and rarely exceeds five. Using large scales could pose a problem later in the method, by creating a large amount of decision rules in the decision table (Bohanec et al., 2013). Whenever possible, it is recommended to use preferentially ordered scales (Trdin & Bohanec, 2018), where scale values are ordered from the most undesired (e.g, “low”) to most desired (“high”) properties.

    Each aggregate attribute x1',x2', …,xm', y has an associated decision table (in MCDM also referred to as utility function), denoted U1, U2, …, Um, Uy, respectively. A decision table Ui defines the aggregation of lower-level child attributes of xi' into the attribute xi' itself: Ui: Ux∈Si X→Xi'

    Here, Si ∈{x1, …, xn, x1', …, xm'} represents the set of child attributes of xi'.

    A decision table Ui consists of rows that contain all possible combinations of values of attributes in Si; thus, the table contains Πx∈Si |X| rows, where |X| represents the size (number of values) of the value scale of x. In the table, each row is associated with a value of xi' that specifies the function output for that input value combination. One can observe aggregate attributes xi' as interactions between attributes x∈Si. More specifically, a corresponding decision table Ui explains how combinations of attribute values of x influence the decision being made at xi'.

    It is worth noting that decision rules are usually formulated by the decision maker and/or domain expert, and are generally easy to interpret (Bohanec et al., 2013). There are two particularly important properties of decision tables one should strive for while defining them:

    - Completeness: a utility function provides evaluation for all possible combinations of input values, i.e., no row in the table has been left undefined.
    - Consistency: a better value of each preferentially ordered child attribute does not decrease the value of the output attribute. Consequently, a consistent utility function is monotone.

    Once all the above components have been developed, a DEX model can be used to evaluate decision alternatives A1, A2, …, Aq (Figure 1). Initially, each alternative Ai, i=1,…, q, is represented by a vector of input values ⟨vi1, vi2, …, vin ⟩, where vij ∈\in Xj, i=1,…,q, j=1,…,n. These values are recursively aggregated in a bottom-up way, using decision tables defined in the model, eventually producing the value viy ∈ Y, which represents the overall evaluation of Ai. Along the way, the values of aggregate attributes x1',…, xm' are produced, too, which represent partial evaluations of Ai corresponding to each xi'. Partial evaluations are often used to trace the evaluation process and may help in justifying the decision.
    '''
)