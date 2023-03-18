from fastapi import FastAPI
from firebase_dir import setup
from pydantic import BaseModel


# app initialize
app = FastAPI()

class UserID(BaseModel):
    uid: str

@app.post("/get_schedule")
def func(user: UserID):
    data = setup.db.collection('users').document(user.uid).get().to_dict()
    return data