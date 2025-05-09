import jwt
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List, Dict, Optional


### Models
class User(BaseModel):
    username: str
    role: str
    subscription_plan: Optional[str]

class Permissions(BaseModel):
    name: str
    description: str
    permissions: List[str]
    usuage_limits: Dict[str, int]

class PlanUpdate(BaseModel):
    description: Optional[str]
    permissions: Optional[List[str]]
    usage_limits: Optional[Dict[str, int]]

    