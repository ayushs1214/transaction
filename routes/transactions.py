from fastapi import APIRouter, HTTPException
from config import client
from database import find_account_by_id, update_account_balance, create_account
from models import TransferRequest, CreateAccountRequest

router = APIRouter()

@router.post("/transfer")
async def transfer_funds(request: TransferRequest):
    async with await client.start_session() as session:
        async with session.start_transaction():
            sender = await find_account_by_id(request.sender_id)
            receiver = await find_account_by_id(request.receiver_id)

            if not sender or not receiver:
                raise HTTPException(status_code=404, detail="Sender or receiver not found")

            if sender["balance"] < request.amount:
                raise HTTPException(status_code=400, detail="Insufficient funds")

            # Perform the transfer
            await update_account_balance(request.sender_id, -request.amount, session)
            await update_account_balance(request.receiver_id, request.amount, session)

    return {"status": "success", "message": "Transfer completed"}

@router.post("/create_account")
async def create_account_endpoint(request: CreateAccountRequest):
    account_id = await create_account(request.name, request.initial_balance)
    return {"status": "success", "account_id": account_id}