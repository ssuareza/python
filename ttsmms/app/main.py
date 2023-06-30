import os
import uuid
import boto3
from botocore.exceptions import ClientError
from .config import Config
from ttsmms import download, TTS
from fastapi import Depends, FastAPI, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

# Initialize configuration.
config = Config()

# Download models.
download("eng", "./model")

# Set aws s3 client.
s3 = boto3.client(
    's3',
    region_name=config.aws_region_name,
    aws_access_key_id=config.aws_access_key_id,
    aws_secret_access_key=config.aws_secret_access_key
)

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


class Speach(BaseModel):
    text: str
    lang: str


@app.post("/", dependencies=[Depends(authenticate)])
async def create_speach(speach: Speach):
    # text-to-speech
    # load model
    model = os.path.join(config.model_path, speach.lang)
    tts = TTS(model)

    # save prediction
    filename = str(uuid.uuid4()) + ".wav"
    wav_file = os.path.join(config.storage_path, filename)
    tts.synthesis(speach.text, wav_path=wav_file)

    # upload to s3
    if config.storage_type == "s3":
        try:
            # upload
            url = "https://" + config.storage_s3_bucket + \
                ".s3.amazonaws.com/" + filename
            s3.upload_file(wav_file, config.aws_s3_bucket, filename)

            # and delete file
            os.remove(wav_file)

            return {"url": url}
        except ClientError as e:
            return {"detail": e}

    return {"detail": "ok"}
