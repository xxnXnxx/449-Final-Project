# Cloud Service Access Management System

## Setup Instructions
1. Clone the repository:
   git clone https://github.com/your-repo

2. Install the required dependencies:
   pip install -r requirements.txt

3. Run the FastAPI server:
   uvicorn app.main:app --reload

4. Open the browser and search http://127.0.0.1:8000/frontend

## API Endpoints

- POST /plans - Create a new subscription plan
- PUT /plans/{planId} - Modify an existing plan
- DELETE /plans/{planId} - Delete a plan
- POST /permissions - Add a new permission
- PUT /permissions/{permissionId} - Modify an existing permission
- DELETE /permissions/{permissionId} - Delete a permission
- POST /subscriptions - Subscribe a user to a plan
- GET /subscriptions/{userId} - Get subscription details for a user
- POST /usage/{userId} - Track API usage for a user
- GET /usage/{userId}/limit - Check if a user has exceeded API limits

## Team Members
- Ian Gabriel
- Peter Wong
- ...Bouyer
