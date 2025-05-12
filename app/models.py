from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from .database import Base


class Plan(Base):
    __tablename__ = "plans"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    permissions = Column(JSON, nullable=False)  # List of API names
    usage_limits = Column(JSON, nullable=False)  # Limits for each API


class Permission(Base):
    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    api_endpoint = Column(String, nullable=False)
    description = Column(String, nullable=True)


class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True, nullable=False)
    plan_id = Column(Integer, ForeignKey("plans.id"))
    plan = relationship("Plan")


class Usage(Base):
    __tablename__ = "usage"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    api_name = Column(String, nullable=False)
    count = Column(Integer, default=0)