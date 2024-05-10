from typing import ClassVar

from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict

api = APIRouter(prefix="/api/v1")


class AddAPIBody(BaseModel):
    number: int

    model_config: ClassVar[ConfigDict] = {
        "json_schema_extra": {"examples": [{"number": 0}]}
    }


class AddAPIResponse(BaseModel):
    result: int

    model_config: ClassVar[ConfigDict] = {
        "json_schema_extra": {"examples": [{"result": 1}]}
    }


@api.post(path="/add", response_model=AddAPIResponse)
def add(body: AddAPIBody) -> AddAPIResponse:
    return AddAPIResponse(result=body.number + 1)


class BadRequestResponse(BaseModel):
    detail: str


app = FastAPI(
    docs_url="/test", redoc_url="/docs", responses={400: {"model": BadRequestResponse}}
)


@app.exception_handler(exc_class_or_status_code=Exception)
def generic_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    response = BadRequestResponse(detail=str(object=exc))
    return JSONResponse(status_code=400, content=response.model_dump())


app.include_router(router=api)
