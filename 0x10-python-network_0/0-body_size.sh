#!/bin/bash
# script that takes URL, sends a request to that URL, and displays the size
# of the body
curl -w "%{size_download}\n" $1 -s -o test
