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
    # This is a simple counter for API usage
    # In a real-world scenario, you might want to track timestamps or other metadata
    # for each usage event
    # For simplicity, we are just counting the number of times an API is called

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)  # Store hashed passwords
    subscription_id = Column(Integer, ForeignKey("subscriptions.id"))
    subscription = relationship("Subscription")
    # Add any other user-related fields as needed

class UserProfile(Base):
    __tablename__ = "user_profiles"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    address = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    user = relationship("User")

class UserSettings(Base):
    __tablename__ = "user_settings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    setting_name = Column(String, nullable=False)
    setting_value = Column(String, nullable=False)
    user = relationship("User")

class UserActivity(Base):
    __tablename__ = "user_activity"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    activity_type = Column(String, nullable=False)
    activity_timestamp = Column(String, nullable=False)  # Use a proper datetime type in production
    user = relationship("User")

class UserRole(Base):
    __tablename__ = "user_roles"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    role_name = Column(String, nullable=False)
    user = relationship("User")

class UserPermission(Base):
    __tablename__ = "user_permissions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    permission_name = Column(String, nullable=False)
    user = relationship("User")

class UserNotification(Base):
    __tablename__ = "user_notifications"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    notification_type = Column(String, nullable=False)
    notification_message = Column(String, nullable=False)
    notification_timestamp = Column(String, nullable=False)  # Use a proper datetime type in production
    user = relationship("User")

class UserSubscriptionHistory(Base):   
    __tablename__ = "user_subscription_history"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    plan_id = Column(Integer, ForeignKey("plans.id"))
    subscription_start_date = Column(String, nullable=False)  # Use a proper datetime type in production
    subscription_end_date = Column(String, nullable=False)  # Use a proper datetime type in production
    user = relationship("User")
    plan = relationship("Plan")
    
class UserFeedback(Base):
    __tablename__ = "user_feedback"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    feedback_text = Column(String, nullable=False)
    feedback_timestamp = Column(String, nullable=False)  # Use a proper datetime type in production
    user = relationship("User")
    