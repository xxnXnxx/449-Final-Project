# Cloud Service Access Management System

## Project Description

The **Cloud Service Access Management System** is a backend system designed to manage access to cloud services based on user subscriptions. It allows administrators to create and manage subscription plans and permissions, while customers can subscribe to plans and access cloud services within their subscription limits. The system enforces usage limits and provides role-based access control (RBAC).

---

## Features

### Admin Functions:
- **Subscription Plan Management**:
  - Create, modify, and delete subscription plans.
  - Plans include attributes like name, description, permissions (API access), and usage limits.
- **Permission Management**:
  - Add, modify, and delete permissions for APIs.

### Customer Functions:
- **User Subscription Handling**:
  - Subscribe to a plan.
  - View current subscription details and usage statistics.
- **Access Control**:
  - Access cloud services based on subscription permissions and usage limits.

### Usage Tracking:
- Track API usage for each user.
- Enforce limits by temporarily restricting access to APIs once limits are exceeded.

---

## Setup Instructions

### Prerequisites:
- Python 3.9 or higher
- SQLite (or any other database supported by SQLAlchemy)

### Setup Instructions
1. Clone the repository:
   git clone https://github.com/your-repo

2. Install the required dependencies:
   pip install -r requirements.txt

3. Run the FastAPI server:
   uvicorn app.main:app --reload

4. Open the browser and search http://127.0.0.1:8000/frontend

### Team Members
- Ian Gabriel
- Peter Wong
- ...Bouyer
