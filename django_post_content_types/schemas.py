from pydantic import BaseModel, EmailStr, Field, ConfigDict


class JSONDataSchema(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "John Doe",
                "email": "john@example.com",
                "age": 30
            }
        }
    )

    name: str = Field(min_length=2, max_length=100, description="User's full name")
    email: EmailStr = Field(description="Valid email address")
    age: int = Field(ge=0, le=150, description="User's age")

