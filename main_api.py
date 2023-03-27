from fastapi import FastAPI
from backend import setup
from pydantic import BaseModel
import pandas as pd
from typing import Optional
import backend.scheduler as scheduler
from datetime import date


# app initialize
app = FastAPI()


class UserID(BaseModel):
    uid: str
    appliance_data: str


@app.post("/")
def func(user: UserID):
    data = setup.db.collection('users').document(user.uid).get().to_dict()
    appliance_set = user.appliance_data
    dt = str(date.today())
    try:
        test = data[appliance_set][dt]
        return test
    except:
        schedule = scheduler.schedule(data[appliance_set])
        setup.db.collection('users').document(user.uid).set(
            {appliance_set: {dt: schedule}}, merge=True)
        return data[appliance_set][dt]
