FROM python:3.8
# Not -alpine because: https://stackoverflow.com/a/58028091/651139
# `docker build` should be run from `monitoring` (the parent folder of this folder)
RUN apt-get update && apt-get install openssl && apt-get install ca-certificates
RUN mkdir -p /app/operator_authorization_qualifier
COPY requirements.txt /app/operator_authorization_qualifier/requirements.txt
WORKDIR /app/operator_authorization_qualifier
RUN pip install -r requirements.txt
RUN rm -rf __pycache__
ENV PYTHONPATH /app
ARG version
ENV CODE_VERSION=$version
ENTRYPOINT []
