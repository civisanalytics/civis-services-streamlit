#!/usr/bin/env bash

set -e

python --version

cd "$APP_DIR"

if [ -d "$REPO_PATH_DIR" ]; then
    echo "$REPO_PATH_DIR is a directory. Your Streamlit app's entry point is assumed to be at $REPO_PATH_DIR/app.py."
    export APP_PY="app.py"
elif [ -f "$REPO_PATH_DIR" ]; then
    echo "$REPO_PATH_DIR is a file, assumed to be the entry point of your Streamlit app."
    export APP_PY="$(basename "$REPO_PATH_DIR")"
    export REPO_PATH_DIR="$(dirname "$REPO_PATH_DIR")"
else
    echo "The specified path '$REPO_PATH_DIR' does not exist." >&2
    echo "Please ensure that the path is correct and that it points to your Streamlit app's directory or file." >&2
    exit 1
fi

cd "$REPO_PATH_DIR"

if [ ! -f "$APP_PY" ]; then
    echo "The expected Streamlit app entry point file is not found at $REPO_PATH_DIR/$APP_PY" >&2
    exit 1
fi

if [ ! -f requirements.txt ]; then
    echo "The file 'requirements.txt' is not found at $REPO_PATH_DIR. " \
         "For your app's stability, it is strongly recommended that requirements.txt be provided " \
         "to pin the exact version of the Python dependencies." >&2
else
    echo "Installing dependencies from requirements.txt"
    uv pip install --no-progress --no-cache -r requirements.txt
fi

if [ -f pyproject.toml ]; then
    echo "Installing python package defined by pyproject.toml"
    uv pip install --no-deps -e .
fi

uv pip list

echo "Running Streamlit application"
streamlit run "$APP_PY"
