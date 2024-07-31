from fastapi import FastAPI
from routes.transactions import router as transactions_router

app = FastAPI()

app.include_router(transactions_router, prefix="/transactions", tags=["transactions"])

# Run the application
# Use the following command to start the server:
# uvicorn main:app --reload
