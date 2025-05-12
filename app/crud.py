from sqlalchemy.orm import Session
from .models import Plan, Permission, Subscription, Usage
from .schemas import PlanCreate, PermissionCreate, SubscriptionCreate
from fastapi import HTTPException


def create_plan(db: Session, plan: PlanCreate):
    db_plan = Plan(
        name=plan.name,
        description=plan.description,
        permissions=plan.permissions,
        usage_limits=plan.limits,
    )
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan


def modify_plan(db: Session, plan_id: int, plan: PlanCreate):
    db_plan = db.query(Plan).filter(Plan.id == plan_id).first()
    if not db_plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    db_plan.name = plan.name
    db_plan.description = plan.description
    db_plan.permissions = plan.permissions
    db_plan.usage_limits = plan.limits
    db.commit()
    db.refresh(db_plan)
    return db_plan


def delete_plan(db: Session, plan_id: int):
    db_plan = db.query(Plan).filter(Plan.id == plan_id).first()
    if not db_plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    db.delete(db_plan)
    db.commit()
    return {"message": "Plan deleted successfully"}


def add_permission(db: Session, permission: PermissionCreate):
    db_permission = Permission(
        name=permission.name,
        api_endpoint=permission.api_endpoint,
        description=permission.description,
    )
    db.add(db_permission)
    db.commit()
    db.refresh(db_permission)
    return db_permission


def modify_permission(db: Session, permission_id: int, permission: PermissionCreate):
    db_permission = db.query(Permission).filter(Permission.id == permission_id).first()
    if not db_permission:
        raise HTTPException(status_code=404, detail="Permission not found")
    db_permission.name = permission.name
    db_permission.api_endpoint = permission.api_endpoint
    db_permission.description = permission.description
    db.commit()
    db.refresh(db_permission)
    return db_permission


def delete_permission(db: Session, permission_id: int):
    db_permission = db.query(Permission).filter(Permission.id == permission_id).first()
    if not db_permission:
        raise HTTPException(status_code=404, detail="Permission not found")
    db.delete(db_permission)
    db.commit()
    return {"message": "Permission deleted successfully"}


def subscribe_to_plan(db: Session, user_id: int, plan_id: int):
    db_subscription = Subscription(user_id=user_id, plan_id=plan_id)
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription


def get_user_subscription(db: Session, user_id: int):
    subscription = db.query(Subscription).filter(Subscription.user_id == user_id).first()
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return subscription


def track_api_usage(db: Session, user_id: int, api_name: str):
    db_usage = db.query(Usage).filter(Usage.user_id == user_id, Usage.api_name == api_name).first()
    if not db_usage:
        db_usage = Usage(user_id=user_id, api_name=api_name, count=1)
        db.add(db_usage)
    else:
        db_usage.count += 1
    db.commit()
    db.refresh(db_usage)
    return db_usage


def check_limit(db: Session, user_id: int):
    subscription = db.query(Subscription).filter(Subscription.user_id == user_id).first()
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    plan = subscription.plan
    usage = db.query(Usage).filter(Usage.user_id == user_id).all()
    usage_summary = {u.api_name: u.count for u in usage}
    for api_name, limit in plan.usage_limits.items():
        if usage_summary.get(api_name, 0) >= limit:
            return {"message": f"Limit exceeded for {api_name}"}
    return {"message": "Usage is within limits"}

def get_all_plans(db: Session):
    return db.query(Plan).all()
def get_all_permissions(db: Session):
    return db.query(Permission).all()
def get_all_subscriptions(db: Session):
    return db.query(Subscription).all()
def get_all_usages(db: Session):
    return db.query(Usage).all()
def get_plan_by_id(db: Session, plan_id: int):
    db_plan = db.query(Plan).filter(Plan.id == plan_id).first()
    if not db_plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return db_plan
def get_permission_by_id(db: Session, permission_id: int):
    db_permission = db.query(Permission).filter(Permission.id == permission_id).first()
    if not db_permission:
        raise HTTPException(status_code=404, detail="Permission not found")
    return db_permission
def get_subscription_by_id(db: Session, subscription_id: int):
    db_subscription = db.query(Subscription).filter(Subscription.id == subscription_id).first()
    if not db_subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return db_subscription
def get_usage_by_id(db: Session, usage_id: int):
    db_usage = db.query(Usage).filter(Usage.id == usage_id).first()
    if not db_usage:
        raise HTTPException(status_code=404, detail="Usage not found")
    return db_usage
def get_plan_by_name(db: Session, plan_name: str):
    db_plan = db.query(Plan).filter(Plan.name == plan_name).first()
    if not db_plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return db_plan
def get_permission_by_name(db: Session, permission_name: str):
    db_permission = db.query(Permission).filter(Permission.name == permission_name).first()
    if not db_permission:
        raise HTTPException(status_code=404, detail="Permission not found")
    return db_permission
def get_subscription_by_user_id(db: Session, user_id: int):
    db_subscription = db.query(Subscription).filter(Subscription.user_id == user_id).first()
    if not db_subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return db_subscription
def get_usage_by_user_id(db: Session, user_id: int):
    db_usage = db.query(Usage).filter(Usage.user_id == user_id).all()
    if not db_usage:
        raise HTTPException(status_code=404, detail="Usage not found")
    return db_usage
def get_usage_by_api_name(db: Session, api_name: str):
    db_usage = db.query(Usage).filter(Usage.api_name == api_name).all()
    if not db_usage:
        raise HTTPException(status_code=404, detail="Usage not found")
    return db_usage
def get_usage_by_api_name_and_user_id(db: Session, api_name: str, user_id: int):
    db_usage = db.query(Usage).filter(
        Usage.api_name == api_name, Usage.user_id == user_id
    ).first()
    if not db_usage:
        raise HTTPException(status_code=404, detail="Usage not found")
    return db_usage
