from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional

# Run the app with: uvicorn main:app --reload

# Initialize FastAPI app
app = FastAPI()


# Define a Pydantic model for user data
class User(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None  # Optional field with default None
    is_active: bool = True  # Default value


# Create an API endpoint to receive and validate user data
@app.post("/users/")
async def create_user(user: User):
    # Pydantic automatically validates the input data
    # If validation fails, FastAPI returns a 422 error with details
    return {"message": "User created successfully", "user_data": user.model_dump()}
