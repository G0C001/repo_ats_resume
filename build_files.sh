python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt

sudo dnf update -y
sudo dnf install -y libgobject-2.0.so libpango-1.0.so libfontconfig.so libpangoft2-1.0.so

pip3 install django Weasyprint

echo "Setup completed successfully!"
