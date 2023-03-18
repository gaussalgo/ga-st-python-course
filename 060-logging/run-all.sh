#!/bin/bash

set -e

./010-init.py
./015-basic.py
./016-factory.py
./020-layers.py
./030-graylog.py
./040-rmh.py
./050-config.py
./060-secrets-task.py

echo
echo
echo "OK: $(pwd)/$(basename $0)"
echo
