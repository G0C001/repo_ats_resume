#!/bin/bash

# Create and activate a new virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip to the latest version to avoid issues with dependencies
pip install --upgrade pip

# Install Python dependencies
pip install -r requirements.txt

# Check if apt-get is available
if command -v apt-get > /dev/null; then
    # Update package lists and install necessary system dependencies
    apt-get update
    apt-get install -y libnss3 libnspr4 libgbm1
elif command -v apk > /dev/null; then
    # For Alpine Linux
    apk add --no-cache libnss3 libnspr4 libgbm1
elif command -v yum > /dev/null; then
    # For CentOS/RHEL
    yum install -y nss nspr libgbm
else
    echo "No compatible package manager found. Please install the dependencies manually."
    exit 1
fi

# Install Playwright and its browsers
pip install playwright
playwright install-deps

# Optionally, you can deactivate the virtual environment after installation
# deactivate

echo "Setup completed successfully!"
