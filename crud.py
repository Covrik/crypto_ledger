from models import TransactionCreate, TransactionOut
from storge import transactions
import random
from datetime import datetime

def create_transaction(transaction:TransactionCreate):
    new_t={
        "id":random.randint(10**4,10**6),
        "timestamp":datetime.now().isoformat()
    }
    new_t.update(transaction.model_dump())

    transactions.append(TransactionOut(**new_t))
    return new_t







