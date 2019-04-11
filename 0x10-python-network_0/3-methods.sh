#!/bin/bash
# shows methods
curl -I -X OPTIONS -s "$1" | grep Allow: | cut -b 8-100
