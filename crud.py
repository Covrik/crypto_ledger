from models import TransactionCreate, TransactionOut, BlockCreate, BlockOut
from storge import transactions
import random
from datetime import datetime
import hashlib

def create_transaction(transaction:TransactionCreate):
    new_t={
        "id":random.randint(10**4,10**6),
        "timestamp":datetime.now()
    }
    new_t.update(transaction.model_dump())

    transactions.append(TransactionOut(**new_t))
    return new_t



def create_block(block: BlockCreate):

    hash = hashlib.sha256(str(block.model_dump()).encode()).hexdigest()
    new_b = {
        "id":random.randint(10**7,10**9),
        "hash": f"hash_{hash}",
        "timestamp": datetime.now(),
        "is_mined": False
    }
    new_b.update(block.model_dump())
    return new_b



def get_transactions():
    return transactions


# b1 = BlockCreate(previous_hash = '', transactions_ids = [2359832885,8765792,259802352], miner = "майнер тест")
# b1_full = create_block(b1)
# print(b1_full)

# b2 = BlockCreate(previous_hash = b1_full["hash"], transactions_ids = [2359832885,8765792,259802352], miner = "майнер тест")
# b2_full = create_block(b2)
# print(b2)
