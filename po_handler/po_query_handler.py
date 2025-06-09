# po_handler/po_query_handler.py

def handle_po_query(query, memory):
    # Dummy logic for demo purposes
    if "pending" in query.lower():
        return memory.get("pending", "You have 5 pending POs.")
    elif "last po" in query.lower() or "latest po" in query.lower():
        return memory.get("last_po", "The last PO was issued to Vendor ABC on 2025-05-25.")
    return "Sorry, I couldn't understand the query."
