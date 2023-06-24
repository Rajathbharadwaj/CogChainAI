from brownie import Staker, accounts

from brownie.network.gas.strategies import LinearScalingStrategy

from reactpy import component, run, web, hooks,html
import json


gas_strategy = LinearScalingStrategy("10 gwei", "50 gwei", 1.1)
account = accounts.load('rinkeby')
def deploy():
    staker = Staker.deploy(accounts[0], {'from': accounts[0], "gas_price": gas_strategy})
    period = staker.claimPeriodLeft()
    print(period)

def main():
    deploy()
    print('Hello')


mui = web.module_from_template(
    "react@^17.0.0",
    "@material-ui/core@4.12.4",
    "@metamask/sdk",
    fallback="⌛",
)
Button = web.export(mui, "Button")


def ViewButtonEvents():
    event, set_event = hooks.use_state(None)

    return html.div(
        Button(
            {
                "color": "primary",
                "variant": "contained",
                "onClick": lambda event: set_event(event),
            },
            "Click Me!",
        ),
        html.pre(json.dumps(event, indent=2)),
    )


run(ViewButtonEvents)
