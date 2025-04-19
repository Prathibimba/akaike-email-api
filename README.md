Email Classification for Support Team
Project Overview
This project is an Email Classification System for a support team. The system categorizes incoming support emails into predefined categories while ensuring that personal information (PII) is masked before processing. After classification, the masked data is restored to its original form.

Objective
Email Classification: Classify support emails into categories like Billing Issues, Technical Support, Account Management, etc.

Personal Information Masking: Mask personal information such as names, email addresses, phone numbers, etc., before processing using custom methods (not relying on Large Language Models).

API Deployment: Deploy the solution as an API that accepts an email, masks PII, classifies the email, and returns the result.

Key Features
Email Classification:

Classifies emails into categories like Billing Issues, Technical Support, and more.

Uses machine learning models (e.g., Naïve Bayes, SVM, Random Forest).

PII Masking:

Masks personally identifiable information (PII) such as full names, emails, phone numbers, etc., before processing.

Uses Named Entity Recognition (NER), regular expressions (Regex), or other custom methods.

API:

A POST request accepts an email body and returns the classification, along with a masked version of the email.

Deployment:

Deployed on Hugging Face Spaces for public access.

Requirements
Python: 3.7+

Libraries:

fastapi - For API development.

spacy - For Named Entity Recognition (NER) and PII masking.

scikit-learn - For model training and classification.

pandas, numpy - For data processing.

uvicorn - ASGI server to run the FastAPI app.

You can install the dependencies by running:

bash
Copy
Edit
pip install -r requirements.txt
Setup Instructions
1. Clone the Repository
Clone the repository to your local machine:

bash
Copy
Edit
git clone https://github.com/Prathibimba/akaike-email-api.git
cd akaike-email-api
2. Install Dependencies
Make sure you have all the required libraries installed:

bash
Copy
Edit
pip install -r requirements.txt
3. Run the API Locally
To run the application locally:

bash
Copy
Edit
uvicorn app:app --reload
Visit http://127.0.0.1:8000/docs to access the Swagger UI, where you can test the API.

API Usage
Endpoint: /classify/
Method: POST

Request Body:

json
Copy
Edit
{
  "email_body": "Hello, my name is John Doe, and my email is johndoe@example.com. I have an issue with my billing."
}
Response:

json
Copy
Edit
{
  "input_email_body": "Hello, my name is John Doe, and my email is johndoe@example.com. I have an issue with my billing.",
  "list_of_masked_entities": [
    {
      "position": [18, 28],
      "classification": "full_name",
      "entity": "John Doe"
    },
    {
      "position": [48, 69],
      "classification": "email",
      "entity": "johndoe@example.com"
    }
  ],
  "masked_email": "Hello, my name is [full_name], and my email is [email]. I have an issue with my billing.",
  "category_of_the_email": "Billing Issues"
}
4. Deploy on Hugging Face Spaces
The API is deployed on Hugging Face Spaces. You can access the live deployment here:

Hugging Face Space Link

Model Selection
Model Used: A traditional machine learning model (e.g., Naïve Bayes, SVM) for classifying support emails into different categories.

Training Data: The provided dataset of emails containing various support requests.

Report
Approach
PII Masking: The project uses custom methods (like regular expressions and NER) to detect and mask PII such as names, emails, and phone numbers in incoming emails.

Email Classification: A traditional machine learning model was chosen for classifying emails into support categories based on labeled data.

Challenges: Masking PII without relying on large models was tricky, but using NER and Regex provided a solid solution.

License
This project is licensed under the MIT License - see the LICENSE file for details.
