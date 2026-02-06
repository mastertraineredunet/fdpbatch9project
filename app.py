import streamlit as st
import pandas as pd
st.title("Student's Placement Data")
data = st.file_uploader("Upload Student's Data")
if data is not None:
    st.success("File Uploaded")
    df = pd.read_csv(data)
    st.dataframe(df)
    st.success("thanyou")