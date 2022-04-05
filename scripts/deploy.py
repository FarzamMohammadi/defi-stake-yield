from scripts.helpful_scripts import get_account
from brownie import DappToken, TokenFarm, network, config
from web3 import Web3

KEPT_BALANCE = Web3.ToWei(100, "ether")


def deploy_token_farm_and_dapp_token():
    account = get_account()
    dapp_token = DappToken.deploy({"from": account})
    token_farm = TokenFarm.deploy(
        dapp_token.address,
        {"from": account},
        pubished_source=config["networks"][network.show_active()]["verify"],
    )
    tx = dapp_token.transfer(
        token_farm.address, dapp_token.totalSupply() - KEPT_BALANCE
    )
    tx.wait(1)
    add_allowed_tokens()


def add_allowed_tokens(token_farm, dict_of_allowed_tokens, account):
    pass


def main():
    deploy_token_farm_and_dapp_token()