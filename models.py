from pydantic import BaseModel
from pydantic import BaseModel, Field

class TransferRequest(BaseModel):
    sender_id: str
    receiver_id: str
    amount: float

class CreateAccountRequest(BaseModel):
    name: str
    initial_balance: float = Field(gt=0, description="Initial balance must be greater than zero")