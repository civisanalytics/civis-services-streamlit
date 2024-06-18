#!/usr/bin/env bash

set -e

python --version

cd "$APP_DIR/$REPO_PATH_DIR"

if [ ! -f app.py ]; then
    echo "The required file 'app.py' is not found at $APP_DIR/$REPO_PATH_DIR" >&2
    exit 1
fi

if [ ! -f requirements.txt ]; then
    echo "The file 'requirements.txt' is not found at $APP_DIR/$REPO_PATH_DIR. " \
         "For your app's stability, it is strongly recommended that requirements.txt be provided " \
         "to pin the exact version of the Python dependencies." >&2
else
    echo "Installing dependencies from requirements.txt"
    pip install --progress-bar off --no-cache-dir -r requirements.txt
fi

if [ -f pyproject.toml ]; then
    echo "Installing python package defined by pyproject.toml"
    pip install --no-deps -e .
fi

pip list

echo "Running Streamlit application"
streamlit run app.py
