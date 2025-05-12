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
    count: int = 0  # Default to 0 for new usage records

class UserCreate(BaseModel):
    username: str
    email: str
    password: str  # Store hashed passwords
    subscription_id: int = None  # Optional, can be set later

class UserProfileCreate(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    address: str = None  # Optional
    phone_number: str = None  # Optional

class UserSettingsCreate(BaseModel):
    user_id: int
    settings: Dict[str, str]  # Dictionary to store user settings