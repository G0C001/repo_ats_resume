# python3 -m venv myenv
# source myenv/bin/activate
# pip install -r requirements.txt

dnf install -y libgobject-2.0.so libpango-1.0.so libfontconfig.so libpangoft2-1.0.so
echo "dll installed"
pip3 install django Weasyprint

echo "Setup completed successfully!"
