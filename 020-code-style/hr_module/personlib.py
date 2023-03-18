from pydantic import BaseModel

class Person(BaseModel):
    name: str
    city: str
