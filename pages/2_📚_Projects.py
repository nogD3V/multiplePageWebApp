import streamlit as st

tab1, tab2, tab3 = st.tabs(["P1", "P2", "P3"])

with tab1:
    st.header("APP ABOUT...")
    st.write("All the things about the app")
    st.image("./images/2Q.jpg")

with tab2:
    st.header("WEB ABOUT...")
    st.write("All the things about the app")
    st.image("./images/2E.jpg")

with tab3:
    st.header("GRAPH ABOUT...")
    st.write("All the things about the app")
    st.image("./images/2R.jpg")
