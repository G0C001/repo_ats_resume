set -e

echo "Starting the build process..."

if [ ! -d "myenv" ]; then
    python3 -m venv myenv
    echo "Virtual environment created."
else
    echo "Virtual environment already exists."
fi

# Activate the virtual environment
source myenv/bin/activate
echo "Virtual environment activated."

# Install dependencies from requirements.txt
if [ -f "requirements.txt" ]; then
    pip3 install -r requirements.txt
    echo "Python dependencies installed."
else
    echo "requirements.txt not found, skipping Python dependencies installation."
fi

# Update system packages
dnf update -y
echo "System packages updated."

# Install required libraries
dnf install -y glib2 pango fontconfig
echo "Required libraries installed."

