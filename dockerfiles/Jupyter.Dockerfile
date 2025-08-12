# syntax=docker/dockerfile:1

FROM quay.io/jupyter/base-notebook

COPY ./dockerfiles/requirements.txt .

RUN pip install -r requirements.txt

