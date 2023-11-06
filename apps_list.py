import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(layout="wide")
st.header("Dashboard Apps")
st.write("created by Jaspreet Kaur")

col1_head,col2_head,col3_head=st.columns(3)
col10,col11,col12=st.columns(3)
col7,col8,col9=st.columns(3)
col1,col2,col3=st.columns(3)
col4,col5,col6=st.columns(3)

with col10:
    st.info("tweets_sentiment_analysis")

with col11:
    st.info("Beauty products are analyzed")

with col12:
    st.link_button("UB_Beauty_Dashboard", "https://ubdashboard.streamlit.app/Skin_Type")


with col7:
    st.info("tweets_sentiment_analysis")

with col8:
    st.info("Sentiments of tweets are analyzed for different US airlines")

with col9:
    st.link_button("tweets_analysis_dashbaord", "https://tweetssentimentanalysis.streamlit.app/")


with col1_head:
    st.subheader("Name of Project")

with col2_head:
    st.subheader("Description")

with col3_head:
    st.subheader("Link to the Project")

with col1:
    st.info("sales_analytics_dashboard")

with col2:
    st.info("sales_analytics_dashboard is built using streamlit and contain filters based on which analytics are generated")

with col3:
    st.link_button("sales_analytics_dashboard", "https://salesanalyticsdashboard-nddhpybwhoaerrswpp8rax.streamlit.app/")
    
with col4:
    st.info("uber_pickups")

with col5:
    st.info("uber_pickups is built using streamlit and analyze about timings when people book more cabs")

with col6:
    st.link_button("uber_pickups_dashboard", "https://yt6hwgasmti9kt4vfs4jiu.streamlit.app/")


