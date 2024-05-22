import streamlit as st 
from data import skills, work_exp, education
from sidebar import show_sidebar
from streamlit_timeline import timeline

st.set_page_config(layout="wide", page_title="Personal Website")

# Adding spacing between buttons
st.markdown("""
    <style>
        div.stButton {
            margin-right: 10px; /* Adjust the margin as needed */
        }
    </style>
""", unsafe_allow_html=True)


# SIDEBAR 
show_sidebar()

# BODY    
st.subheader("About me")
st.write("Data Scientist & Physicist, experienced in managing projects at the nexus of scientific inquiry and data-driven decision making.")
st.markdown("<br>", unsafe_allow_html=True) 

left,middle,right =st.columns(3)
with left:
    with open("static/DimitraGkogkouResume.pdf", "rb") as file:
        btn = st.download_button(
                label="Download CV",
                data=file,
                file_name="DimitraGkogkouResume.pdf",
                mime ="pdf"
            )
with middle:
    st.link_button("My GitHub", "https://github.com/Dimi-G")
with right:
    st.link_button("LinkedIn", "https://www.linkedin.com/in/dimitra-gkogkou/")


st.subheader("Tech Skills")
columns = st.columns(4)
for i, skill in enumerate(skills['Tech Skills']):
    col_index = i % 4
    button= columns[col_index].button(skill)
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Science Skills")
sorted_scskills = sorted(skills['Science Skills'], key=len)
columns = st.columns(3)
for i, skill in enumerate(sorted_scskills):
    col_index = i % 3
    button= columns[col_index].button(skill)
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Transferable Skills")
sorted_sfskills = sorted(skills['Soft Skills'], key=len)
columns = st.columns(3)
for i, skill in enumerate(sorted_sfskills):
    col_index = i % 3
    button= columns[col_index].button(skill)
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Work Experience")
dates_w= [2024,2019,2017,2013]
selected_year_w = st.select_slider("Timeline", options=dates_w)
with st.expander("Professional Experience"):
    years = work_exp[selected_year_w]["Years"]
    company = work_exp[selected_year_w]["Company"]
    positions = work_exp[selected_year_w]["Position"]
    tasks = work_exp[selected_year_w]["Tasks"]
    st.write(f"**Years:** {years}")
    st.write(f"**Company:** {company}")
    st.write(f"**Position:**")
    for position in positions:
        st.write(f"- {position}")    
    st.write("**Tasks:**")
    for task in tasks:
        st.write(f"- {task}")
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Education")
dates_e = [2017,2013,2011,2004]
selected_year_e= st.select_slider("Timeline", options=dates_e)
with st.expander("Studies"):
    years= education[selected_year_e]["Years"]
    degree = education[selected_year_e]["Degree"]
    university = education[selected_year_e]["University"]
    thesis = education[selected_year_e]["Thesis"]
    st.write(f"**Years:** {years}")
    st.write(f"**Degree:** {degree}")
    st.write(f"**University:** {university}")
    st.write(f"**Thesis:** {thesis}")
st.markdown("<br>", unsafe_allow_html=True)

