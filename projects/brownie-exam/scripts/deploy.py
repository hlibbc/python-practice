from brownie import Storage, accounts

def main():
    acct = accounts[0]  # Ganache가 자동으로 제공하는 계정
    storage = Storage.deploy({"from": acct})
    print("Storage contract deployed at:", storage.address)
