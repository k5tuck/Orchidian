from block import Block

class Blockchain():
    def __init__(self):
        self.chain = []
        self.all_transactions = []
        self.genesis_block()
    
    def genesis_block(self):
        self.Block = Block(transactions = [], previous_hash = 0)
        self.chain.append(self.Block)
    
    def addblock(self, transactions):
        previous_hash = self.chain[len(self.chain)-1].hash
        newblock = Block(transactions, previous_hash)
        proof = self.proof_of_work(newblock)
        self.chain.append(newblock)
        return proof, newblock

    def printblocks(self):
        for i in range(len(self.chain)):
            currentblock = self.chain[i]
            print("Block {} {}".format(i, currentblock))
            currentblock.printblock()
            
    def validatechain (self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if current.hash != current.generated_hash():
                print("The current hash of the block {} does not equal the generated hash of the block.".format(i))
                return False
            if current.previous_hash != previous.generated_hash():
                print("The previous block's hash, block {}, does not equal the previous hash value stored in the current block.".format(i-1))
                return False
        return True
    
    def proof_of_work(self,block, difficulty=2):
        proof = block.generated_hash()
        while (proof[:2] != "0" * difficulty):
            block.nonce += 1
            proof = block.generated_hash()
        correct_proof = proof
        block.nonce = 0
        return correct_proof