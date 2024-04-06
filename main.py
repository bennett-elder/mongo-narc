import pymongo
import sys
import os
from datetime import datetime, timezone
from time import sleep

from slack_sdk.webhook import WebhookClient

mongo_datetime_format = '%Y-%m-%d %H:%M:%S.%f%z'
narc_start_time = datetime.now(timezone.utc)
print(f'not worried about any docs before {narc_start_time}')

slack_url = os.environ.get('SLACK_URL')
db_url = os.environ.get('DB_URL')
db_name = os.environ.get('DB_NAME')
table_name = os.environ.get('TABLE_NAME', 'comments')
match_column_name = os.environ.get('MATCH_COLUMN_NAME', 'blurb')
match_string = os.environ.get('MATCH_STRING')
date_column_name = os.environ.get('DATE_COLUMN_NAME', 'date')
wait_between_checks = int(os.environ.get('WAIT_BETWEEN_CHECKS', 60))
id_column_name = os.environ.get('ID_COLUMN_NAME', 'id')
report_message = os.environ.get('REPORT_MESSAGE', 'event happened')

try:
  client = pymongo.MongoClient(db_url)
except:
  print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
  sys.exit(1)

print(db_name)
print(table_name)
print(match_column_name)
print(match_string)
print(date_column_name)
print(wait_between_checks)
print(id_column_name)
print(report_message)

db = client[db_name]

table = db[table_name]

while True:
  result = table.find({match_column_name:match_string, date_column_name: { '$gt' : narc_start_time}}).sort({date_column_name:1})
  if result:    
    for doc in result:
      blurb = doc[match_column_name]
      date = doc[date_column_name]
      narc_start_time = doc[date_column_name]
      id = doc[id_column_name]
      output = f"{id}: {report_message}"
      print(output)
      slack_client = WebhookClient(slack_url)
      response = slack_client.send(text=output)
      assert response.status_code == 200
      assert response.body == "ok"
  print(f"{datetime.now(timezone.utc)} sleeping for {wait_between_checks}")
  sleep(wait_between_checks)