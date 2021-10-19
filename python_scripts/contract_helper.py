import logging
from eth_typing import abi
from web3 import Web3
from hash_helper import hash_from_file
import json


class ContractHelper:

    def __init__(self, url, address):

        self.w3 = Web3(Web3.HTTPProvider(url))

        with open(r'./build/contracts/StudentCertificate.json') as abi_file:
            self.abi = json.load(abi_file)['abi']
        self.address = self.w3.toChecksumAddress(address)
        self.contract = self.w3.eth.contract(address=address, abi=self.abi)

    def add_hash(self, id, hash):

        trasaction = self.contract.functions.add_hash(id, hash).buildTransaction({
            'nonce': self.w3.eth.getTransactionCount('0x92BE98536C2DA43E09c1753069348C69601788e0'),
            'from': '0x92BE98536C2DA43E09c1753069348C69601788e0'
        })
        signed_transaction = self.w3.eth.account.signTransaction(
            trasaction, '1c0164ad06573657d2acaf250a6d7c55b30eb12562d2408cdfb618a108d0c295')
        trasaction_hash = self.w3.eth.sendRawTransaction(
            signed_transaction.rawTransaction)
        self.w3.eth.wait_for_transaction_receipt(trasaction_hash)
        return trasaction_hash

    def get_hash(self, id):
        return self.contract.functions.get_hash(id).call()

    


if __name__ == '__main__':
    import random
    import string
    logging.basicConfig(level=logging.INFO, filename='log.csv', format='%(message)s')
    url = 'https://rinkeby.infura.io/v3/afb8a4a2e1274b8db453e3d621f137b3'
    address = '0xc3b7DbA76FC3818ae82C02e4112D0eDf57f5bC7f'

    contract = ContractHelper(url, address)
    # print(contract.get_hash(1000002))
    # contract.add_hash(1, 'afsfsfsgfssdgsgafaf')
    # print(contract.contract.functions.get_owner().call())
    # contract.contract.functions.add_admin('0x92BE98536C2DA43E09c1753069348C69601788e0').call()
    # print(contract.get_hash(1000008))

    k = 'a'
    for i in range(15):
        transaction_hash = contract.add_hash(600+i, k)
        gas_used = contract.w3.eth.getTransactionReceipt(transaction_hash).gasUsed

        logging.info(f'{len(k)},{gas_used}')
        print(gas_used)
        for _ in range(len(k)):
            k += random.choice(string.ascii_letters)