#!/bin/bash

set -e

(cd ./040-decorators/; ./run-all.sh)
(cd ./050-exceptions/; ./run-all.sh)
(cd ./060-logging/; ./run-all.sh)

echo
echo
echo "OK: $(pwd)/$(basename $0)"
echo
