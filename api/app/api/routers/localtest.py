import typing as t
from fastapi import APIRouter, Response, HTTPException
from app.core.w3_utils import get_local_test_accounts
from app.core.exceptions import ProviderValueError
from uvicorn.config import logger

localtest_router = r = APIRouter()


@r.get(
    "/get_accounts",
    response_model=t.List[str]
)
async def get_accounts(
    response: Response,
):
    """
    Get accounts of local for using with network_id ETHLOCALTEST
    """

    try:
        ret = get_local_test_accounts()

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

    return ret
