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
dnf install -y glib2 pango fontconfig glibc-langpack-en
echo "Required libraries installed."

# Check if the locale is available
if ! locale -a | grep -q "en_US.utf8"; then
    echo "Generating en_US.UTF-8 locale..."
    localedef -v -c -i en_US -f UTF-8 en_US.UTF-8
    echo "Locale en_US.UTF-8 generated."
else
    echo "Locale en_US.UTF-8 is already available."
fi

# Set locale environment variables
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
echo "Locale set to en_US.UTF-8."

echo "Build completed successfully!"
