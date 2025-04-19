import pandas as pd
from utils import mask_pii
from models import train_model

# Step 1: Load the raw data
df = pd.read_csv('data/combined_emails_with_natural_pii.csv')

# Step 2: Mask PII
masked_emails = []
entity_logs = []

for email in df['email']:
    masked, entities = mask_pii(email)
    masked_emails.append(masked)
    entity_logs.append(entities)

df['masked_email'] = masked_emails
df['entity_log'] = entity_logs

# Step 3: Save the processed data
df.to_csv("data/processed_emails.csv", index=False)
print("✅ Masked email data saved to data/processed_emails.csv")

# Step 4: Train the model on the processed data
train_model("data/processed_emails.csv")
print("✅ Model trained and saved as email_classifier.pkl")
