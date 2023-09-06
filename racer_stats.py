import streamlit as st
import pandas as pd
st.markdown("# Racer Page 🎈")
st.sidebar.markdown("# This is Racer Page 🎈")

st.write(' # Mariokart *Stats Website*')


df_racer=pd.read_csv('data/racer_stats.csv')

# st.write(df_racer)
st.dataframe(df_racer.style.highlight_max(color='teal', axis=0,subset=['Speed'])
             .highlight_min(color='red', axis=0,subset=['Speed']))

st.line_chart(df_racer,x='Speed',y= ['Acceleration','Weight','Handling'])
st.header("Racer Speed does not seem to correlate to number of races the win")
x=st.slider('How many racers to show',1,len(df_racer))
st.write("Racers by Speed")
df_fastest_Racers=df_racer[['Character','Speed']].sort_values("Speed",ascending=False).iloc[0:x]
st.dataframe(df_fastest_Racers)
