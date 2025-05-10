import jwt
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Text, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from typing import List, Dict, Optional

### ==== Explaination of classes in relation to one another ============================

# each user has a name of a subscription plan. 
# if the user is logged in, they will try to access an endpoint. 
# that endpoint will find that user's subscription plan, 
# check the subscription plan's list of permissions, 
# and if the name of that permission is not in the subscription plan's permission list, 
# it will throw an error

### ====================================================================================


# Note: I am using XAMPP to run my local server, if you aren't your URL may look different
DATABASE_URL = "mysql+pymysql://root:@localhost/cloud_access_db"
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

### Pydantic Models (validates response)
class User(BaseModel):
    username: str
    role: str
    subscription_plan: Optional[str]

class SubscriptionPlan(BaseModel):
    name: str
    description: str
    permissions: List[str]
    usuage_limits: Dict # {"admin": -1, "subcription1": 20, "subscription2": 10, etc..}

class Permission(BaseModel):
    name: str
    endpoint: str   # we decouple name and endpoint so, 
                    # if we change the URL we don't have to change every plan
    description: str

class PlanUpdate(BaseModel):
    description: Optional[str]
    permissions: Optional[List[str]]
    usage_limits: Optional[Dict[str, int]]

### SQLAlchemy Models


### API routes
@app.put("/plans/{plan_id}")
def update_plan(plan_id: int, plan_data: PlanUpdate, db: Session = Depends(get_db)):
    plan = db.query(SubscriptionPlan).filter(SubscriptionPlan.id == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")

    if plan_data.description is not None:
        plan.description = plan_data.description
    if plan_data.permissions is not None:
        plan.permissions = plan_data.permissions
    if plan_data.usage_limits is not None:
        plan.usage_limits = plan_data.usage_limits

    db.commit()
    db.refresh(plan)
    return {"message": "Plan updated successfully", "plan": {
        "id": plan.id,
        "name": plan.name,
        "description": plan.description,
        "permissions": plan.permissions,
        "usage_limits": plan.usage_limits
    }}