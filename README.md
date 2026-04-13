# MinIO AWS S3 (Python)

Lightweight Python examples for common MinIO (S3-compatible) operations: connect, create bucket, upload, download, list, delete, and generate a presigned URL.

## Features
- Connect to a MinIO server
- Create a bucket if it does not exist
- Upload and download objects
- List objects in a bucket
- Delete objects
- Generate a presigned URL

## Prerequisites
- Python 3.10+ installed
- A running MinIO server (local or remote)

## Installation
1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configure MinIO Connection
Update the connection details in `minIO/connect.py`:
- Endpoint (host:port)
- `access_key`
- `secret_key`
- `secure` (set `True` for HTTPS)

## Usage
The examples are wired in `main.py`. Uncomment the operation you want to run.

```bash
python main.py
```

### Typical flows
- Create a bucket: `create_new_bucket()`
- Upload a file: `upload_obj()`
- Download a file: `download_obj()`
- List objects: `get_objects()`
- Get a presigned URL: `get_obj_url()`
- Delete an object: `delete_obj()`

## Project Structure
- `main.py` entry point for running examples
- `minIO/` individual MinIO operations

## Notes
- Bucket names and object keys are currently hardcoded in each module. Adjust them to match your MinIO setup.
- Credentials are also hardcoded for simplicity. For production usage, move credentials to environment variables or a secrets manager.
