import streamlit as st
import pandas as pd
#import plotly.express as px



st.title('cric info app')


def load_data(file_path):
    df=pd.read_csv(file_path)
    return df

data_path='./newcricinfo.csv'
df=load_data(data_path)
st.dataframe(df)
country_match=df.groupby('country')['Matches'].sum().sort_values().reset_index()

st.sidebar.header('Filteres')
country=st.sidebar.multiselect('select country',options=df['country'].unique(),default=df['country'].unique())
#duration=st.sidebar.slider('select Duration'.df['Duration'].min(),df['Duration'].max())
#player=st.sidebar.multiselect()
filter_df=df[
    (df['country'].isin(country))
]
st.dataframe(filter_df)

total_runs=filter_df['Runs'].sum()
total_matches=filter_df['Matches'].sum()
total_hundreds=filter_df['100'].sum()
total_sixes=filter_df['6s'].sum()
total_player=filter_df['Player'].nunique()

col1,col2,col3,col4,col5,=st.columns(5)

with col1:
    st.metric(label='total_runs',value=total_runs)
with col2:
    st.metric(label='total_matches',value=total_matches)
with col3:
    st.metric(label='total_hundreds',value=total_hundreds)
with col4:
    st.metric(label='total_sixes',value=total_sixes)
with col5:
    st.metric(label='total_player',value=total_player)


"""fig_country=px.pie(
    country_match,
    names='country',
    values='Matches',
    title='country wise matches'

)
st.plotly_chart(fig_country)

country_match=df.groupby('country')['Matches'].sum().sort_values().reset_index()

fig = px.bar(df, x='country', y='Matches', title="country wise matches")
st.plotly_chart(fig)


country_match=df.groupby('Matches')['Runs'].sum().sort_values().reset_index()
fig_runs=px.pie(
    country_match,
    names='Matches',
    values='Runs',
    title='Matches wise Runs'

)
st.plotly_chart(fig_runs)"""
