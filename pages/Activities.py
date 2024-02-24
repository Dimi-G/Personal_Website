import streamlit as st
import pandas as pd
from data import coordinates

st.set_page_config(layout="wide", page_title="Personal Website")


# SIDEBAR 
with st.container():
    st.sidebar.image("static/DG.jpg")
    st.sidebar.header("Dr. Dimitra Gkogkou")
    st.sidebar.write("Aspiring Data Scientist  \n Physicist  \n Scientific Editor  \n")


with open("static/CV_Gkogkou.pdf", "rb") as file:
    btn = st.sidebar.download_button(
            label="Download CV",
            data=file,
            file_name="CV_Gkogkou.pdf",
            mime ="pdf"
          )
    
st.sidebar.link_button("My GitHub", "https://github.com/Dimi-G")
st.sidebar.link_button("LinkedIn", "https://www.linkedin.com/in/dimitra-gkogkou/")

#BODY
st.subheader("Seminars")
#include Kaggle, LinkedIn etc
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Presentations")
st.write("Over the years,  I have presented my work in numerous local and global conferences and seminars.")
df=pd.DataFrame(coordinates, columns =['latitude', 'longitude'] )
st.map(df)
st.image("static/WINS3.png", width=500, caption= "Women in Natural Sciences Summer School 2023 'Pointers for paper publishing & Integrity in the Research & Publishing Process'")
st.markdown("<br>", unsafe_allow_html=True)

#Photos from Wins, Title of seminar. Older wiley presentations, something from Phd Conferences
st.subheader("Publications")
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Distinctions")
st.markdown("<br>", unsafe_allow_html=True)
#Lindau Nobel Meeting
#Dissertations Prize Finalist
#Best Poster Award

st.subheader("Activism")
#https://web.archive.org/web/20210922215731/https://year2018.iscientist.de/
#https://thessalonikipride.com/en/thessaloniki-pride-2012/
#https://www.facebook.com/photo/?fbid=288606367913248&set=a.288605214580030&locale=el_GR
st.markdown("<br>", unsafe_allow_html=True)