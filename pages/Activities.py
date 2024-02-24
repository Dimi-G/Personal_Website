import streamlit as st
import pandas as pd
from data import coordinates, workshops, publications, distinctions

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
st.subheader("Presentations")
st.write("Over the years, I had the luck to present my work in numerous local and global conferences and seminars.")
df=pd.DataFrame(coordinates, columns =['latitude', 'longitude'] )
st.map(df)
st.markdown("<br>", unsafe_allow_html=True)
ll, lr,rl, rr =st.columns(4)
with lr:
    st.image("static/WINS3.png", width=500, caption= "Women in Natural Sciences Summer School 2023 'Pointers for paper publishing & Integrity in the Research & Publishing Process'.")
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Seminars")
st.write("I am invested in continuous learning. Here is a list of workshops I have completed:")
for workshop in workshops:
    st.write(f"- {workshop}")
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Publications")
with st.expander("List to Academic Publications"):
    for publication in publications:
        st.link_button(label = f'{publication["title"]}- {publication["journal"]}({publication["year"]})',url=publication["url"])
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Distinctions")
for distinction in distinctions:
    st.write(f"- {distinction}")

lc,lrc,rlc,rc =st.columns(4)
with lrc:
    st.image("static/Lindau.jpg", width=500, caption="Meeting Physics Nobelists, Prof. such as Donna Strickland, at Lindau Nobel Meeting 2019.")
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Activism")
left, right = st.columns(2)
with left:
    st.link_button("Co-organizer of I,Scientist 2018 - The conference on gender, career paths & networking", url="https://web.archive.org/web/20210922215731/https://year2018.iscientist.de/")
    st.image("static/Iscientist.jpg", caption= "400 scientists joined for 2 days of presentations, workshops and career fair.")
with right:
    st.link_button("Co-organizer of the first Pride in Thessaloniki (2012)", url="https://thessalonikipride.com/en/thessaloniki-pride-2012/")
    st.image("static/pride.jpg", caption="Around 2000 brave gathered for a historical first Thessaloniki Pride in 2012, an event that now attracts 18 thousand participants.")
st.markdown("<br>", unsafe_allow_html=True)