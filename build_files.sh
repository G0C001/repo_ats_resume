python3 -m venv myenv
source myenv/bin/activate
pip3 install -r requirements.txt

# Update the system and install necessary development libraries using dnf
dnf update -y
dnf install -y glib2 pango fontconfig

echo "Setup completed successfully!"