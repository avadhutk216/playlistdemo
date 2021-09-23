
from sqlite3 import OperationalError
from fastapi import APIRouter
from fastapi import HTTPException


from Providers.input_processing_provider import InputProcessingProvider

input_processing_router = APIRouter()


@input_processing_router.post("/")
async def process_input():
    try:
        input_processing_provider = InputProcessingProvider()
        input_processing_provider.process("playlist.json")
        return "complete"
    except OperationalError as e:
        raise HTTPException(status_code=500,
                            detail="Some error occurred while processing data;"
                                   "Please check if the input data is in correct format and try again")
    except Exception as e:
        raise HTTPException(status_code=500,
                            detail="Some error occurred while processing data")


@input_processing_router.get("/")
async def process_input():
    return "accessed"
