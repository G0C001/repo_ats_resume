# Create and activate a new virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip to the latest version to avoid issues with dependencies
pip install --upgrade pip

# Install Python dependencies
pip install -r requirements.txt

# Install Playwright and its browsers
pip install playwright
python -m playwright install
