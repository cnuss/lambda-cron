import json
import datetime


def handle(event, context):
    return {
        "message": "Your function executed successfully at %s" % datetime.datetime.now(),
        "event": event
    }
