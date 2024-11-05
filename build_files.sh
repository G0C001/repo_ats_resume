export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
if [ -f "requirements.txt" ]; then
    pip3 install -r requirements.txt
    echo "Python dependencies installed."
else
    echo "requirements.txt not found, skipping Python dependencies installation."
fi
dnf install -y pango cairo gdk-pixbuf2 libffi


# Update system packages
dnf update -y
echo "System packages updated."

# Install required libraries
dnf install -y glib2 pango fontconfig
echo "Required libraries installed."

