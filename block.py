import datetime
from hashlib import sha256

class Block():
    def __init__(self, transactions, previous_hash, nonce = 0):
        self.timestamp = datetime.datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.generated_hash()

    def printblock(self):
        print("Timestamp: ", self.timestamp)
        print("Transactions: ", self.transactions)
        print("Current Hash: ", self.hash)
        print("Previous Hash: ", self.previous_hash)
        print('\n')

    def generated_hash(self):
        contents = str(self.timestamp) + str(self.transactions) + str(self.nonce) + str(self.previous_hash)
        hash = sha256(contents.encode())
        return hash.hexdigest()
