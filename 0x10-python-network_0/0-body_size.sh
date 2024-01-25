#!/bin/bash
# displays body of the response 
curl -s "$1" | wc -c
