from brownie import Storage, accounts

def test_storage_set_and_get():
    acct = accounts[0]
    storage = Storage.deploy({"from": acct})

    storage.set(99, {"from": acct})
    assert storage.get() == 99
