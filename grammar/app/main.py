import torch
from .config import Config
from fastapi import FastAPI, Depends, HTTPException, Request, Response
from fastapi.security import OAuth2PasswordBearer
from starlette import status
from polyglot.detect import Detector
from gramformer import Gramformer

# Initialize configuration.
config = Config()


def set_seed(seed):
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


set_seed(1212)

# 1=corrector, 2=detector (not implemented yet)
gf = Gramformer(models=1, use_gpu=False)

# Initialize api.
app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

# Set token authentication.
token = OAuth2PasswordBearer(tokenUrl="token")


def authenticate(token: str = Depends(token)) -> bool:
    if token != config.api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Basic"},
        )

# Define endpoints.


@app.get("/healthz")
def healthz():
    # health check
    return {"detail": "ok"}


@app.get("/auth", dependencies=[Depends(authenticate)])
def auth():
    # authentication check
    return {"detail": "Authenticated"}


@app.post("/", dependencies=[Depends(authenticate)])
async def root(request: Request, response: Response):
    # grammar correction
    jsonResponse = await request.json()
    sentence = jsonResponse["text"]
    lang = Detector(sentence).languages[0].code

    # only english is supported
    if lang != "en":
        return {"detail": lang + " not supported"}
    else:
        return {"detail": gf.correct(sentence, max_candidates=1)}
