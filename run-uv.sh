#!/bin/bash
# Launch Django dev server with uv
poetry run uvicorn nistaiapp.asgi:application --reload --host 0.0.0.0 --port 8000
