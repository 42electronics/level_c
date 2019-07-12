#!/bin/bash

gpio -g mode 13 out
gpio -g mode 19 out
gpio -g mode 26 out

gpio -g write 13 1
gpio -g write 19 0
gpio -g write 26 0

echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""
