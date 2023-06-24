from brownie import Staker, accounts

from brownie.network.gas.strategies import LinearScalingStrategy


gas_strategy = LinearScalingStrategy("10 gwei", "50 gwei", 1.1)

def deploy():
    Staker.deploy(accounts[0], {'from': accounts[0], "gas_price": gas_strategy})
def main():
    deploy()
    print('Hello')
