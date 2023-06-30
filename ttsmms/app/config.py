import os


class Config:
    api_key = os.getenv("API_KEY")
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_region_name = os.getenv("AWS_REGION_NAME")
    aws_s3_bucket = os.getenv("AWS_S3_BUCKET")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    model_path = os.getenv("MODEL_PATH")
    storage_path = os.getenv("STORAGE_PATH")
    storage_type = os.getenv("STORAGE_TYPE")
