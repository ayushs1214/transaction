from bson import ObjectId
from config import accounts_collection

async def find_account_by_id(account_id: str):
    return await accounts_collection.find_one({"_id": ObjectId(account_id)})

async def update_account_balance(account_id: str, amount: float, session):
    await accounts_collection.update_one(
        {"_id": ObjectId(account_id)},
        {"$inc": {"balance": amount}},
        session=session
    )

async def create_account(name: str, initial_balance: float):
    account = {"name": name, "balance": initial_balance}
    result = await accounts_collection.insert_one(account)
    return str(result.inserted_id)