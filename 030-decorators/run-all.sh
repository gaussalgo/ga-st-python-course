#!/bin/bash

set -e

./010-motivation-1.py
timeout 10 ./020-motivation-2.py &
while ! nc -z localhost 5000; do
  sleep 0.1
done
curl --fail http://localhost:5000
curl --fail http://localhost:5000/test
curl --fail http://localhost:5000/len/message
./030-basic.py
./040-simple-retry.py || true
./050-simple-retry-params.py || true
./060-timer-task.py


echo
echo
echo "OK: $(pwd)/$(basename $0)"
echo
