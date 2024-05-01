#!/usr/bin/env bash

set -e

python --version

cd "$APP_DIR/$REPO_PATH_DIR"

if [ ! -f app.py ]; then
    echo "The required file 'app.py' is not found at $APP_DIR/$REPO_PATH_DIR" >&2
    exit 1
fi

if [ ! -f requirements.txt ]; then
    echo "The file 'requirements.txt' is not found at $APP_DIR/$REPO_PATH_DIR." \
         "For your app's stability, it is strongly recommended that requirements.txt be provided" \
         "to pin the exact version of the Python dependencies." >&2
else
    echo "Installing dependencies"
    pip install -r requirements.txt
fi

if [[ ! -n $(command -v streamlit) ]]; then
    echo "The 'streamlit' command doesn't exist." \
         "The likely reason is that the package 'streamlit' isn't specified in requirements.txt." \
         "It is strongly recommended that 'streamlit' be pinned with a specific version in requirements.txt" \
         "for your app's stability." \
         "For now, 'streamlit' is going to be installed by running 'pip install streamlit'." >&2
    pip install streamlit
fi

if [ -f pyproject.toml ]; then
    echo "Installing python package defined by pyproject.toml"
    pip install --no-deps -e .
fi

pip cache purge

echo "Running Streamlit application"
streamlit run app.py
