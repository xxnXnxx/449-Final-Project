from app.database import engine
from app.models import Base, Plan 

# Drop all tables
Base.metadata.drop_all(bind=engine)

# Recreate all tables
Base.metadata.create_all(bind=engine)

print("✅ Database reset complete.")
