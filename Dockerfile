FROM --platform=linux/x86_64 python:3.12.3-slim AS base
LABEL maintainer=opensource@civisanalytics.com

# Supress pip user warnings:
# https://stackoverflow.com/a/72551258
ENV PIP_ROOT_USER_ACTION=ignore

RUN apt-get update && apt-get install -y \
    git

WORKDIR /app

# Environmental variables that must be set when deploying
# the Streamlit service on Civis Platform.
# For all Streamlit config options:
# https://docs.streamlit.io/develop/api-reference/configuration/config.toml
ENV STREAMLIT_CLIENT_SHOW_ERROR_DETAILS=false \
    STREAMLIT_SERVER_PORT=3838 \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

FROM base AS production
COPY ./entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

FROM base AS test
COPY ./demo_app/ /app/demo_app/

# Defaults to production as the final stage
FROM production
