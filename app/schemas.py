from pydantic import BaseModel
from typing import List, Dict


class PlanCreate(BaseModel):
    name: str
    description: str
    permissions: List[str]  # List of API names
    limits: Dict[str, int]  # Limits for each API


class PermissionCreate(BaseModel):
    name: str
    api_endpoint: str
    description: str


class SubscriptionCreate(BaseModel):
    user_id: int
    plan_id: int


class UsageCreate(BaseModel):
    user_id: int
    api_name: str