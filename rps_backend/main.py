from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from rps_backend import constants, api
from rps_backend.config import settings

app: FastAPI = FastAPI(debug=settings.DEBUG, title="rps-backend")

app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=constants.ALLOW_ORIGINS,
    allow_credentials=constants.ALLOW_CREDENTIALS,
    allow_methods=constants.ALLOW_METHODS,
    allow_headers=constants.ALLOW_HEADERS,
)
app.include_router(api.api_router)
