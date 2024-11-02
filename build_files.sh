#!/bin/sh

# Check if apt-get is available
if command -v apt-get > /dev/null; then
    apt-get update && apt-get install -y libnss3 libnspr4 libgbm1
elif command -v apk > /dev/null; then
    apk add --no-cache libnss3 libnspr4 libgbm1
elif command -v yum > /dev/null; then
    yum install -y nss nspr libgbm
else
    echo "No compatible package manager found. Please install the dependencies manually."
    exit 1
fi
