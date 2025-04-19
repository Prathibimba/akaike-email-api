import pandas as pd
import re

# Load dataset
def load_data(path):
    return pd.read_csv(path)

# Define PII patterns
PII_PATTERNS = {
    "full_name": r"\b([A-Z][a-z]+ [A-Z][a-z]+)\b",
    "email": r"\b[\w.-]+@[\w.-]+\.\w+\b",
    "phone_number": r"\b\d{10}\b",
    "dob": r"\b\d{2}[/-]\d{2}[/-]\d{4}\b",
    "aadhar_num": r"\b\d{4} \d{4} \d{4}\b",
    "credit_debit_no": r"\b(?:\d{4}[- ]?){4}\b",
    "cvv_no": r"\b\d{3}\b",
    "expiry_no": r"\b(0[1-9]|1[0-2])\/\d{2}\b"
}

def mask_pii(text):
    entity_list = []
    masked_text = text
    for entity, pattern in PII_PATTERNS.items():
        for match in re.finditer(pattern, text):
            start, end = match.span()
            entity_list.append({
                "position": [start, end],
                "classification": entity,
                "entity": match.group()
            })
            masked_text = masked_text.replace(match.group(), f"[{entity}]")
    return masked_text, entity_list
