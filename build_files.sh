python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt

# Update the system and install necessary development libraries using dnf
sudo dnf update -y
sudo dnf install -y glib2 pango fontconfig

pip3 install django Weasyprint

echo "Setup completed successfully!"