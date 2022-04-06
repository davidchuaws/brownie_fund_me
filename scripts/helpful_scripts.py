from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    account = get_account()
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": account})
    print("Mocks Deployed!")