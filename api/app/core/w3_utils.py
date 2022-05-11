from web3 import Web3, EthereumTesterProvider
from eth_tester import EthereumTester
from .exceptions import ProviderValueError


# factory to get connection to node
def get_provider(conn: dict) -> Web3:

    # nicer as a switch statement
    if conn["config_options"]["provider_type"] == 'HTTPProvider':
        provider = Web3.HTTPProvider(conn["config_options"]["url"])
    elif conn["config_options"]["provider_type"] == 'EthereumTesterProvider':
        provider = EthereumTesterProvider()
    elif conn["config_options"]["provider_type"] == 'IPCProvider':
        provider = Web3.IPCProvider(conn["config_options"]["url"])
    elif conn["config_options"]["provider_type"] == 'WebsocketProvider':
        provider = Web3.WebsocketProvider(conn["config_options"]["url"])
    else:
        # should probably be a custom exception
        raise ProviderValueError("Provider type not known")

    return Web3(provider)


# wrapper for the is address
def is_address(w3: Web3, address: str) -> bool:

    return w3.isAddress(w3.toChecksumAddress(address))


# wrapper for getting the balance
def get_balance(w3: Web3, address: str) -> int:

    try:
        wei = w3.eth.get_balance(w3.toChecksumAddress(address))
    except ValueError as e:
        # this should be more specific but in general will address issue
        raise ProviderValueError(str(e))

    return w3.fromWei(wei, 'ether')


# wrapper for getting the eth tester accounts
def get_local_test_accounts():
    t = EthereumTester()

    return t.get_accounts()
