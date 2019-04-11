#!/bin/bash
# delete request to the URL and displays body of response
curl -sI -X DELETE "$1"
