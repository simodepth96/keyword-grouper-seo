import streamlit as st
import pandas as pd

# Function to read uploaded files (CSV or XLSX)
def load_file(uploaded_file):
    if uploaded_file is not None:
        file_extension = uploaded_file.name.split(".")[-1]
        
        if file_extension == "csv":
            return pd.read_csv(uploaded_file)
        elif file_extension in ["xls", "xlsx"]:
            return pd.read_excel(uploaded_file, engine="openpyxl")  # Use openpyxl for xlsx
        else:
            st.error("Unsupported file format. Please upload a CSV or XLSX file.")
            return None
    return None

# Streamlit UI
st.title("Keyword Grouper SEO App")
st.subheader("⬆️ Upload Keywords File (CSV or XLSX)")

uploaded_file = st.file_uploader("Upload your file", type=["csv", "xlsx"])  # Allow XLSX

if uploaded_file:
    data = load_file(uploaded_file)
    
    if data is not None:
        st.write("Preview of Uploaded File:")
        st.dataframe(data.head())

        # Allow user to select the keyword column dynamically
        columns = data.columns
        keyword_column = st.selectbox("Select Keyword Column:", columns)

        st.success("File loaded successfully! Now you can process it.")
