# Cloud Service Access Management System

## Authors
**Ian Gabriel Vista, Peter Wongprasert, & ?**

## Project Overview

The **Cloud Service Access Management System** is a backend system designed to manage user access to cloud services based on their subscription plans. Customers access cloud services according to their assigned plan, while administrators manage the subscription plans, permissions, and user access.

This system enforces limits based on the subscription plan, restricting access to services once the usage limits are exceeded. The system includes role-based access control (RBAC) to allow admins to manage subscriptions, permissions, and API access.

## Features

- **Subscription Plan Management**: Admins can create, modify, and delete subscription plans.
- **Permission Management**: Admins can add, modify, and delete permissions for APIs.
- **User Subscription Handling**: Customers can subscribe to plans, view their subscription details, and track their usage. Admins can modify user subscriptions.
- **Access Control**: The system checks if a customer’s request is within the scope of their plan and denies access if limits are exceeded or permissions are not granted.
- **Usage Tracking and Limit Enforcement**: Tracks API usage for each user and temporarily restricts access if the usage limit is reached.


## Dependencies

- install dependencies: `pip install fastapi uvicorn sqlalchemy pymysql`

fastapi: run fast api using `uvicorn app:app --reload`
uvicorn: async gateway server for fastapi
sqlalchemy: object relational mapper for structuring code objects into database relational models. 
    i.e. changes object data to push onto db.
pymysql: lightweight MySQL driver for Python 