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
    pip install --progress-bar off -r requirements.txt
fi

for package in streamlit civis; do
  if [[ ! -n $(command -v $package) ]]; then
      echo "The package '$package' wasn't installed, so we're installing its latest version. " \
           "It is strongly recommended that '$package' be pinned with a specific version in requirements.txt " \
           "for your app's stability." >&2
      pip install --progress-bar off $package
  fi
done

if [ -f pyproject.toml ]; then
    echo "Installing python package defined by pyproject.toml"
    pip install --no-deps -e .
fi

pip cache purge

echo "Running Streamlit application"
streamlit run app.py
