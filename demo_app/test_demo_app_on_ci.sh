#!/usr/bin/env bash

# This test script is meant to be run on CI only.

set -e

uv pip install --no-progress --no-cache -r /app/demo_app/requirements.txt && \
uv pip list -v && \
python -u << HERE
from streamlit.testing.v1 import AppTest
app = AppTest.from_file("/app/demo_app/app.py", default_timeout=10)
app.run()
assert not app.exception
print("demo app ran successfully")
HERE
