import streamlit as st
import pandas as pd

# Sample data (you would replace this with your actual database)
data = {
    'Setting': ['Coastal', 'Coastal'],
    'Constraint': ['Lithology', 'Lithology'],
    'Feature': ['Rocky coast', 'Rocky coast'],
    'Foundation_Type': ['Cables', 'Pipelines'],
    'Lithology': ['Hard substrate', 'Hard substrate'],
    'Relief': ['Steep slopes/margins (>5 degrees)', 'Steep slopes/margins (>5 degrees)'],
    'Engineering_Significance': ['Requires individual WTG siting investigation', 'Requires individual WTG siting investigation'],
    'Geological_Complexity': ['Medium', 'Medium'],
    'Comments': ['Lorem ipsum dolor sit amet consectetur. Aliquam tortor vestibulum praesent enim purus cursus. In facilisi commodo enim ipsum. Non rhoncus aliquam lacus ac ac commodo.', 
                 'Lorem ipsum dolor sit amet consectetur. Aliquam tortor vestibulum praesent enim purus cursus. In facilisi commodo enim ipsum. Non rhoncus aliquam lacus ac ac commodo.']
}

df = pd.DataFrame(data)

st.set_page_config(layout="wide")

st.title("EGDI")

st.header("Geo-Assessment Matrix")

st.write("Explore the database of surficial and subsurface parameters influencing cost, stability and performance of turbines, cables and hubs in shallow and deep waters.")

# Sidebar for filters
st.sidebar.header("Filters")

setting = st.sidebar.selectbox("Setting & Process", df['Setting'].unique())
constraint = st.sidebar.selectbox("Type of constraint", df['Constraint'].unique())
feature = st.sidebar.selectbox("Features", df['Feature'].unique())
foundation_type1 = st.sidebar.selectbox("Foundation type 1", df['Foundation_Type'].unique())
foundation_type2 = st.sidebar.selectbox("Foundation type 2", df['Foundation_Type'].unique())

# Filter the dataframe
filtered_df = df[(df['Setting'] == setting) & 
                 (df['Constraint'] == constraint) & 
                 (df['Feature'] == feature) & 
                 (df['Foundation_Type'].isin([foundation_type1, foundation_type2]))]

# Main content
st.subheader("Surficial and Subsurface Parameters")

col1, col2 = st.columns(2)

with col1:
    st.subheader(foundation_type1)
    foundation1_data = filtered_df[filtered_df['Foundation_Type'] == foundation_type1].iloc[0]
    st.write("**Lithology:**", foundation1_data['Lithology'])
    st.write("**Relief:**", foundation1_data['Relief'])
    st.write("**Engineering Significance:**", foundation1_data['Engineering_Significance'])
    st.write("**Geological Complexity:**", foundation1_data['Geological_Complexity'])
    st.write("**Comments:**", foundation1_data['Comments'])

with col2:
    st.subheader(foundation_type2)
    foundation2_data = filtered_df[filtered_df['Foundation_Type'] == foundation_type2].iloc[0]
    st.write("**Lithology:**", foundation2_data['Lithology'])
    st.write("**Relief:**", foundation2_data['Relief'])
    st.write("**Engineering Significance:**", foundation2_data['Engineering_Significance'])
    st.write("**Geological Complexity:**", foundation2_data['Geological_Complexity'])
    st.write("**Comments:**", foundation2_data['Comments'])

if st.button("Download Report"):
    st.write("Report downloaded (simulated)")