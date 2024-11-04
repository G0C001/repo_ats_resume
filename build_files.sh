python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
apt update
apt install -y libgobject-2.0-0 libpango-1.0-0 libfontconfig1 libpangoft2-1.0-0

# Install pip if not installed
if ! command -v pip3 &> /dev/null
then
    apt install -y python3-pip
fi

# Install Python packages from requirements.txt
pip3 install -r requirements.txt

echo "Setup completed successfully!"