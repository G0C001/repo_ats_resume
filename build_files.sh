if [ -f "requirements.txt" ]; then
    pip3 install -r requirements.txt
    echo "Python dependencies installed."
else
    echo "requirements.txt not found, skipping Python dependencies installation."
fi
dnf install -y pango cairo gdk-pixbuf2 libffi
find / -name libgobject-2.0.so
find / -name libpango-1.0.so



# Update system packages
dnf update -y
echo "System packages updated."

# Install required libraries
dnf install -y glib2 pango fontconfig
echo "Required libraries installed."

