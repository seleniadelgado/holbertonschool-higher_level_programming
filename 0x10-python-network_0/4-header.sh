#!/bin/bash
# sets a header var with a value of 98
curl -s "$1" -X GET -H "X-HolbertonSchool-User-Id: 98"
