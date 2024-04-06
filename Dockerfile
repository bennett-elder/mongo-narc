FROM python:3.11.8

ARG SLACK_URL
ARG DB_URL
ARG DB_NAME
ARG TABLE_NAME="comments"
ARG MATCH_COLUMN_NAME="blurb"
ARG MATCH_STRING
ARG DATE_COLUMN_NAME="date"
ARG WAIT_BETWEEN_CHECKS=60
ARG ID_COLUMN_NAME="id"
ARG REPORT_MESSAGE="event happened"

ENV DB_URL=$DB_URL
ENV DB_NAME=$DB_NAME
ENV TABLE_NAME=$TABLE_NAME
ENV MATCH_COLUMN_NAME=$MATCH_COLUMN_NAME
ENV MATCH_STRING=$MATCH_STRING
ENV DATE_COLUMN_NAME=$DATE_COLUMN_NAME
ENV WAIT_BETWEEN_CHECKS=$WAIT_BETWEEN_CHECKS
ENV ID_COLUMN_NAME=$ID_COLUMN_NAME
ENV REPORT_MESSAGE=$REPORT_MESSAGE


RUN mkdir -p /app
WORKDIR /app
COPY main.py /app
COPY requirements.txt /app
RUN cd /app
RUN pip install -r requirements.txt

WORKDIR /app
CMD ["python", "main.py"]
