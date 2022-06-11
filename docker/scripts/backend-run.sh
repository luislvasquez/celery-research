#!/bin/sh

export FASTAPI_APP=main:app

exec /usr/local/bin/uvicorn "$FASTAPI_APP" --port 8000 --host 0.0.0.0 --proxy-headers --reload