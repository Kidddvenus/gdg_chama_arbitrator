import streamlit as st
import requests
import os

st.set_page_config(page_title="Chama Arbitrator", layout="wide")

st.title("⚖️ Chama Arbitrator")
st.subheader("Neutral Dispute Resolution for Your Cooperative")

query = st.text_input("Enter your dispute or question (Sheng, Swahili, or English):")

if st.button("Resolve"):
    if query:
        backend_url = os.getenv("BACKEND_URL", "http://localhost:8000")
        try:
            # response = requests.post(f"{backend_url}/resolve", json={"query": query})
            st.info("Arbitration in progress...")
            st.success("Draft Ruling: According to Article 4, section 2...")
        except Exception as e:
            st.error(f"Error connecting to backend: {e}")
    else:
        st.warning("Please enter a query.")
