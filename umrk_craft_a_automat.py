import time
from web3 import Web3
from datetime import datetime

# Web3 provider setup
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID'))

# Contract address and ABI
contract_address = '0x...ContractAddress...'
contract_abi = [...ContractABI...]

# Function to get contract instance
def get_contract_instance():
    return w3.eth.contract(address=contract_address, abi=contract_abi)

# Function to get blockchain data
def get_blockchain_data():
    contract_instance = get_contract_instance()
    block_number = w3.eth.block_number
    block_data = w3.eth.get_block(block_number)
    transaction_count = len(block_data.transactions)
    return {
        'block_number': block_number,
        'transaction_count': transaction_count,
        'contract_balance': contract_instance.functions.balanceOf().call()
    }

# Function to update tracker
def update_tracker(data):
    print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]')
    print(f'Block Number: {data["block_number"]}')
    print(f'Transactions: {data["transaction_count"]}')
    print(f'Contract Balance: {data["contract_balance"]}')
    print('---')

# Main loop
while True:
    data = get_blockchain_data()
    update_tracker(data)
    time.sleep(10)  # wait for 10 seconds before next update