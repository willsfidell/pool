import typing as t
from fastapi import APIRouter, Response, HTTPException
from app.db.crud import get_networks, get_network
from app.core import w3_utils
from app.core.exceptions import ProviderValueError
from uvicorn.config import logger
from app.schemas.schemas import Network, NetworkIdEnum, EthAddressType, Balance

networks_router = r = APIRouter()


@r.get(
    "/",
    response_model=t.List[Network]
)
async def get_all_networks(
    response: Response,
):
    """
    list all of the networks configured
    """

    networks = get_networks()

    return networks


@r.get(
    "/get_address_balance",
    response_model=Balance
)
async def get_address_balance(
    response: Response,
    address: EthAddressType,
    network_id: NetworkIdEnum  # In production validation might be done later
):
    """
    Get the balance of an address based
    """

    # get the network details
    network_conn_data = get_network(network_id)

    if network_conn_data is None:
        raise HTTPException(
                    status_code=400,
                    detail="Network unknown"
                )

    try:
        w3 = w3_utils.get_provider(network_conn_data)
        eth = w3_utils.get_balance(w3, address)

    except ProviderValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception as error:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        logger.info(template.format(type(error).__name__, error.args))

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )

    return {"amount": eth, "unit_name": network_conn_data["symbol"]}
