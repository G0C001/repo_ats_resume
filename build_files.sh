#!/bin/bash

# Create and activate a new virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip to the latest version to avoid issues with dependencies
pip install --upgrade pip

# Install Python dependencies
pip install -r requirements.txt

# Update package lists and install necessary system dependencies
apt-get update
apt-get install -y libnss3 libnspr4 libgbm1

# Install Playwright and its browsers
pip install playwright
playwright install-deps

# Optionally, you can deactivate the virtual environment after installation
# deactivate


# Install necessary dependencies

