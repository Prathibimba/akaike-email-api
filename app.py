from fastapi import FastAPI
import uvicorn

# Initialize FastAPI app
app = FastAPI()

# Add a route for the root URL ("/")
@app.get("/")
def read_root():
    return {"message": "Welcome to the Email Classification API 🎉"}

# Example of an existing route for email classification (modify as needed)
@app.post("/classify/")
def classify_email(email: str):
    # Your classification logic goes here
    return {"classification": "Spam"}  # Example response

# Run the application when the script is executed
if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=7860)
