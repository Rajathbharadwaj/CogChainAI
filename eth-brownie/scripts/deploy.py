from brownie import Staker, accounts, network, config

from brownie.network.gas.strategies import LinearScalingStrategy


gas_strategy = LinearScalingStrategy("10 gwei", "50 gwei", 1.1)


def get_account():
    if network.show_active() == 'development':
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])
    

def deploy():
    account = get_account()
    staker = Staker.deploy(account, {'from': account, "gas_price": gas_strategy})
    period = staker.claimPeriodLeft()
    print(period)



def main():
    deploy()
    print('Hello')
