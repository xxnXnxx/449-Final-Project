from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

# Initialize templates and app
templates = Jinja2Templates(directory="templates")
app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Frontend route
@app.get("/frontend", response_class=HTMLResponse)
def get_frontend(request: Request):
    return templates.TemplateResponse("frontend.html", {"request": request})

# Root
@app.get("/")
def read_root():
    return {"message": "Welcome to the Cloud Service Access Management System"}

# Subscription Plan routes
@app.post("/plans")
def create_new_plan(plan: schemas.PlanCreate, db: Session = Depends(get_db)):
    return crud.create_plan(db=db, plan=plan)

@app.get("/plans")
def get_all_plans(db: Session = Depends(get_db)):
    return crud.get_all_plans(db=db)

@app.put("/plans/{plan_id}")
def update_plan(plan_id: int, plan: schemas.PlanCreate, db: Session = Depends(get_db)):
    return crud.modify_plan(db=db, plan_id=plan_id, plan=plan)

@app.delete("/plans/{plan_id}")
def delete_plan(plan_id: int, db: Session = Depends(get_db)):
    return crud.delete_plan(db=db, plan_id=plan_id)

# Permissions routes
@app.post("/permissions")
def add_permission(permission: schemas.PermissionCreate, db: Session = Depends(get_db)):
    return crud.add_permission(db=db, permission=permission)

@app.put("/permissions/{permission_id}")
def modify_permission(permission_id: int, permission: schemas.PermissionCreate, db: Session = Depends(get_db)):
    return crud.modify_permission(db=db, permission_id=permission_id, permission=permission)

@app.delete("/permissions/{permission_id}")
def delete_permission(permission_id: int, db: Session = Depends(get_db)):
    return crud.delete_permission(db=db, permission_id=permission_id)

# Subscriptions routes
@app.post("/subscriptions")
def subscribe_user(subscription: schemas.SubscriptionCreate, db: Session = Depends(get_db)):
    return crud.subscribe_to_plan(db=db, user_id=subscription.user_id, plan_id=subscription.plan_id)

@app.get("/subscriptions/{user_id}")
def get_subscription(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_subscription(db=db, user_id=user_id)

# Usage tracking and limits
@app.post("/usage/{user_id}")
def track_usage(user_id: int, api_name: str, db: Session = Depends(get_db)):
    return crud.track_api_usage(db=db, user_id=user_id, api_name=api_name)

@app.get("/usage/{user_id}/limit")
def check_usage_limit(user_id: int, db: Session = Depends(get_db)):
    return crud.check_limit(db=db, user_id=user_id)

# Sample API services
@app.get("/api/service1")
def service1():
    return {"message": "Service 1 response"}

@app.get("/api/service2")
def service2():
    return {"message": "Service 2 response"}

@app.get("/api/service3")
def service3():
    return {"message": "Service 3 response"}

@app.get("/api/service4")
def service4():
    return {"message": "Service 4 response"}

@app.get("/api/service5")
def service5():
    return {"message": "Service 5 response"}

@app.get("/api/service6")
def service6():
    return {"message": "Service 6 response"}