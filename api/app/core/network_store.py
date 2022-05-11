# this would be replaced by some form of database but simple vars for now
NETWORKS = [
    {
        "id": "ETHLOCALTEST",
        "name": "Ethereum Local Test",
        "symbol": "ETH",
        "config_options": {
            "url": "",
            "provider_type": "EthereumTesterProvider"
        }
    },
    {
        "id": "ETH.RINKEBY",
        "name": "Ethereum Rinkeby Testnet",
        "symbol": "ETH",
        "config_options": {
            "url": "https://rinkeby.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161",
            "provider_type": "HTTPProvider"
        }
    },
    {
        "id": "ETH.ROPSTEN",
        "name": "Ethereum Ropsten Testnet",
        "symbol": "ETH",
        "config_options": {
            "url": "https://ropsten.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161",
            "provider_type": "HTTPProvider"
        }
    },

    {
        "id": "ETH",
        "name": "Ethereum",
        "symbol": "ETH",
        "config_options": {
            "url": "https://eth-rpc.gateway.pokt.network",
            "provider_type": "HTTPProvider"
        }
    },
    {
        "id": "GNOSIS",
        "name": "Gnosis",
        "symbol": "XDAI",
        "config_options": {
            "url": "https://rpc.gnosischain.com",
            "provider_type": "HTTPProvider"
        }
    },
    {
        "id": "OPTIMISM",
        "name": "Optimism",
        "symbol": "ETH",
        "config_options": {
            "url": "https://mainnet.optimism.io",
            "provider_type": "HTTPProvider"
        }

    },
    {
        "id": "OPTIMISM.KOVAN",
        "name": "Optimism Kovan",
        "symbol": "ETH",
        "config_options": {
            "url": "https://kovan.optimism.io",
            "provider_type": "HTTPProvider"
        }
    },

    {
        "id": "ARBITIUM",
        "name": "Arbitium",
        "symbol": "ETH",
        "config_options": {
            "url": "https://rpc.ankr.com/arbitrum",
            "provider_type": "HTTPProvider"
        }

    },
    {
        "id": "ARBITIUM.TESTNET",
        "name": "Arbitium testnet",
        "config_options": {
            "url": "https://rinkeby.arbitrum.io/rpc",
            "provider_type": "HTTPProvider"
        }

    }

]
