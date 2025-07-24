from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional

# Run the app with: uvicorn fastapi_pydantic:app --reload

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
    """
    Pydantic automatically validates the input data
    and raises an error if the data does not conform to the User model.

    Examples:
        >>> from fastapi.testclient import TestClient
        >>> from pybase.api.fastapi_pydantic import app
        >>> client = TestClient(app)
        >>> resp = client.post("/users/", json={"name":"Joe","email":"joe@example.com"})
        >>> resp.status_code
        200
        >>> resp.json()["user_data"]["name"]
        'Joe'
    """
    return {"message": "User created successfully", "user_data": user.model_dump()}
