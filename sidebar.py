import streamlit as st

def show_sidebar():
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
