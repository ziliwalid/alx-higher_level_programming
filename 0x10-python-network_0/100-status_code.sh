#!/bin/bash
# Sends get http and displays response
curl -s -o /dev/null -w "%{http_code}" "$1"
