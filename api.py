from fastapi import FastAPI
from pydantic import BaseModel
from utils import mask_pii
from models import classify_email  

app = FastAPI()

class EmailRequest(BaseModel):
    email_body: str

@app.post("/classify/")
def classify(request: EmailRequest):
    original = request.email_body
    masked, entities = mask_pii(original)
    category = classify_email(masked)

    return {
        "input_email_body": original,
        "list_of_masked_entities": entities,
        "masked_email": masked,
        "category_of_the_email": category
    }
