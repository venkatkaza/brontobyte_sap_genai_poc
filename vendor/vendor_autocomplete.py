# vendor/vendor_autocomplete.py

def get_vendor_suggestions(prefix):
    vendors = ["ABC Pvt Ltd", "Acme Corp", "Zenith Solutions", "Delta Traders", "Nova Enterprises"]
    return [v for v in vendors if v.lower().startswith(prefix.lower())]
