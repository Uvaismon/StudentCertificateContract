from eth_typing import abi
from web3 import Web3
from hash_helper import hash_from_file
import json
import os

class ContractHelper:

    def __init__(self, url, address):

        self.w3 = Web3(Web3.HTTPProvider(url))

        with open(r'./build/contracts/StudentCertificate.json') as abi_file:
            self.abi = json.load(abi_file)['abi']
        self.address = self.w3.toChecksumAddress(address)
        self.contract = self.w3.eth.contract(address=address, abi=self.abi)

    def add_hash(self, id, hash):

        trasaction = self.contract.functions.add_hash(id, hash).buildTransaction({
            'nonce': self.w3.eth.getTransactionCount(os.environ.get('ACCOUNT_ADDRESS'))
        })
        signed_transaction = self.w3.eth.account.signTransaction(trasaction, os.environ.get('ACCOUNT_PRIVATE_KEY'))
        trasaction_hash = self.w3.eth.sendRawTransaction(signed_transaction.rawTransaction)
        self.w3.eth.wait_for_transaction_receipt(trasaction_hash)
        return trasaction_hash

    def get_hash(self, id):
        
        return self.contract.functions.get_hash(id).call()
        self.contract.functions.get_hash(id).call()

    
if __name__ == '__main__':
    url = 'https://rinkeby.infura.io/v3/' + os.environ.get('RINKEBY_KEY')
    address = os.environ.get('CONTRACT_ADDRESS')
    print(address)

    contract = ContractHelper(url, address)
    print(contract.get_hash(4))
    # contract.add_hash(1, 'afsfsfsgfssdgsgafaf')