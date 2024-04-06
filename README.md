# Intro

You ever feel the need to slack notify based on new mongodb activity?

Here's a simple way to do that.

# How to run

```
docker run -it -e DB_NAME=$DB_NAME -e DB_URL=$DB_URL -e SLACK_URL=$SLACK_URL -e MATCH_STRING=$MATCH_STRING bennettelder/mongo-narc:latest
```

DB_NAME is the name of the MongoDB database.

DB_URL is the URL for the MongoDB instance.

SLACK_URL is the webhook URL for posting messages to slack.

MATCH_STRING is the value you expect to find in the MATCH_COLUMN_NAME to trigger a notification.

Other ARGs defined in the Dockerfile determine
* what DATE_COLUMN_NAME it is tracking to make sure it doesn't renotify about old messages after startup
* which ID_COLUMN_NAME to notify about
* what REPORT_MESSAGE to send for the notification
* how long to WAIT_BETWEEN_CHECKS

among other things.

# Worth mentioning

This was built to work with farm-board
