import streamlit as st
import requests

API_URL = "https://genome-api.onrender.com"  # Update with your actual Render backend URL

st.title("🧬 Genome Clustering & Classification")

seq = st.text_area("Paste your RNA Sequence Below:")

if st.button("Classify"):
    res = requests.post(f"{API_URL}/classify", json={"sequence": seq})
    if res.status_code == 200:
        st.success(f"Lineage: {res.json()['lineage']}")
    else:
        st.error("Error from server")

if st.button("Cluster"):
    res = requests.post(f"{API_URL}/cluster", json={"sequence": seq})
    if res.status_code == 200:
        st.success(f"Cluster ID: {res.json()['cluster']}")
    else:
        st.error("Error from server")
