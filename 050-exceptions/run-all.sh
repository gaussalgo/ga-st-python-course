#!/bin/bash

set -e

./010-intro.py
./020-catch.py
./030-own-exp.py
./040-re-raise.py
./050-debug.py || true
./060-auto-pm1.py
./060-auto-pm2.py
./070-price.py || true
./080-sentry.py || true


echo
echo
echo "OK: $(pwd)/$(basename $0)"
echo
