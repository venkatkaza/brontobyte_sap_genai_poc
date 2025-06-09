# app/streamlit_ui.py

import streamlit as st
from po_handler.po_query_handler import handle_po_query
from vendor.vendor_autocomplete import get_vendor_suggestions
from po_handler.po_detail_modal import get_po_details
from retrievers.faiss_memory import init_vector_store
from voice.voice_to_text import transcribe_voice
import pandas as pd

st.set_page_config(page_title="SAP GenAI PoC", layout="wide")
st.title("Brontobyte SAP GenAI Assistant")

memory = init_vector_store()

query = st.text_input("Ask a question about your POs:")
if st.button("Submit Query"):
    result = handle_po_query(query, memory)
    st.write(result)

st.markdown("### 🔍 Vendor Autocomplete")
vendor_input = st.text_input("Start typing a vendor name:")
if vendor_input:
    suggestions = get_vendor_suggestions(vendor_input)
    st.write(suggestions)

st.markdown("### 📦 PO Detail Viewer")
po_id = st.text_input("Enter PO ID:")
if st.button("Get PO Details"):
    details = get_po_details(po_id)
    st.dataframe(pd.DataFrame(details))

st.markdown("### 🎤 Voice Query (Optional)")
if st.button("Start Voice Input"):
    voice_query = transcribe_voice()
    st.write("Transcribed:", voice_query)
