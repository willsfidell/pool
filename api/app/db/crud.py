from typing import List
from app.core.network_store import NETWORKS

def get_networks()->List[dict]:   
    return NETWORKS
    

def get_network(network: str)->dict:

    conn = next((nw for nw in NETWORKS if nw["id"] == network), None)

    return conn
