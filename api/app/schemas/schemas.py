from pydantic import BaseModel, Json,constr
import typing as t
from enum import Enum

EthAddressType = constr(regex="^(0x)?[0-9a-fA-F]{40}$")

class ProviderTypeEnum(str, Enum):
    ETHEREUMTESTERPROVIDER = "EthereumTesterProvider"
    HTTPPROVIDER = "HTTPProvider"
    IPCPROVIDER = "IPCProvider"
    WEBSOCKETPROVIDER = "WebsocketProvider"

class NetworkConfig(BaseModel):
    url: str
    provider_type: ProviderTypeEnum


class Network(BaseModel):
    id: str
    name: str
    symbol: str
    config_options: NetworkConfig

    class Config:
        orm_mode = True

# In production this migth not be a hardcode list
class NetworkIdEnum(str, Enum):
    ETHLOCALTEST = "ETHLOCALTEST"
    ETHRINKEBY = "ETH.RINKEBY"
    ETHROPSTEN = "ETH.ROPSTEN"
    ETH = "ETH"
    GNOSIS = "GNOSIS"
    OPTIMISM = "OPTIMISM"
    OPTIMISMKOVAN = "OPTIMISM.KOVAN"
    ARBITIUM = "ARBITIUM"
    ARBITIUMTESTNET = "ARBITIUM.TESTNET"


class Balance(BaseModel):
    amount: float # could be decimal 
    unit_name: str
