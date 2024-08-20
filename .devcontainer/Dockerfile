FROM python:3.12.1-slim-bullseye
USER root

# Install baseline packages 
RUN apt-get update && \
    apt-get -y install --reinstall ca-certificates && \
    apt-get -y install software-properties-common && \
    apt-get -y install git && \
    pip install --upgrade pip

# Add any python packages you want here
RUN pip install ipykernel jupyter pytest