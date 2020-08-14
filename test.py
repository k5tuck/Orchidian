from blockchain import Blockchain

block_one_transactions = {"sender":"Alice", "receiver": "Bob", "amount":"50"}
block_two_transactions = {"sender": "Bob", "receiver":"Cole", "amount":"25"}
block_three_transactions = {"sender":"Alice", "receiver":"Cole", "amount":"35"}
fake_transactions = {"sender": "Bob", "receiver":"Cole, Alice", "amount":"25"}

#Blockchain Test
first_block = Blockchain()
first_block.addblock(block_one_transactions)
first_block.addblock(block_two_transactions)
first_block.addblock(block_three_transactions)
first_block.printblocks()

#Validation Test
test1 = first_block.chain[2]
test1.transactions = 'receiver bobby'
first_block.validatechain()

